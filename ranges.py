import pickle
import random
import glob
from collections import defaultdict

testing = False

cards = 'AKQJT98765432'

def all_hands():
  l = []
  for i,c1 in enumerate(cards):
    l1 = []
    for j,c2 in enumerate(cards):
      if i < j:
        l1.append(f'{c1}{c2}s')
      elif i == j:
        l1.append(f'{c1}{c2}')
      elif i > j:
        l1.append(f'{c2}{c1}o')
    l.append(l1)
  return l


def get_adjacent_hands(h):
  i = cards.index(h[0])
  j = cards.index(h[1])
  if h[-1] == 'o': # swap i and k for offsuit combos
    k = i
    i = j
    j = k

  adj = []
  all_h = all_hands()
  if i > 0:
    adj += [all_h[i-1][j]]
  if i < 12:
    adj += [all_h[i+1][j]]
  if j > 0:
    adj += [all_h[i][j-1]]
  if j < 12:
    adj += [all_h[i][j+1]]
  return adj
    

# a range is stored as a dict mapping hands to another dict, which maps actions to frequencies.

# give path to a directory containing all gtowiz ranges for every action (except fold) in a spot
def load_gto_range(path):
  range_dict = {}
  for l in all_hands():
    for h in l:
      range_dict[h] = defaultdict(lambda: 0)

  for a in glob.glob(f'{path}/*'):
    action = a.split('/')[-1].split('.')[0]
    string = open(a, 'r').read()

    parse_gto_range(action, string, range_dict)

  for h in range_dict:
    range_dict[h] = dict(range_dict[h])
      
  return range_dict
  

def parse_gto_range(action, string, range_dict):

  # For each entry in the gtowiz format, we convert to suit-agnostic format, and then add the frequency
  # to the hand_dict range for the specified action.
  for h in string.split(','):
    if h[0] == h[2]: # paired
      range_dict[f'{h[0]}{h[2]}'][action] +=  float(h.split(' ')[-1]) / 6 # 6 combos of each paired hand

    elif h[0] != h[2] and h[1] == h[3]: # suited
      range_dict[f'{h[0]}{h[2]}s'][action] += float(h.split(' ')[-1]) / 4 # 4 combos of each suited hand
    else: # offsuit
      range_dict[f'{h[0]}{h[2]}o'][action] += float(h.split(' ')[-1]) / 12 # 12 combos of each offsuit hand



def trim(range_dict):

  # Now, go through all hands and if a combo is 100% folding and there is no adjacent combos
  # that is continueing, remove it from our saved range (so we don't have to bother testing it)

  for hand,actiondict in list(range_dict.items()): # convert to list so can modify range_dict while iterating
    if actiondict: continue
    important=False
    for adjacent_hand in get_adjacent_hands(hand):
      if adjacent_hand in range_dict and range_dict[adjacent_hand]: 
        important=True
        break
    if not important: 
      range_dict.pop(hand)


def test(directory):
  r = load_gto_range(directory)
  trim(r)
  spot = f"{directory.split('/')[-1]}"

  shuffled_hands = list(r.keys())
  random.shuffle(shuffled_hands)
  for hand in shuffled_hands:
    input(f"{spot}: {hand}: ")
    answer = "Correct answer is:" 
    for a in r[hand]:
      answer += f' {a} {r[hand][a]}'
    print(answer)
        



r1 = 'saved_ranges/bu_v_utg_6'
r2 = 'saved_ranges/utg_v_btn_67p5'
r3 = 'saved_ranges/sb_v_bb_24'
r4 = 'saved_ranges/bb_v_button_6'

test(r3)

