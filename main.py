
def count_batteries_by_usage(cycles):
  lowcount=0
  mediumcount=0
  highcount=0
  for i in cycles:
    if i<310:
      lowcount+=1
    elif i<929:
      mediumcount+=1
    else:
      highcount+=1
      
  return f{
    "lowCount": {lowcount},
    "mediumCount": {mediumcount},
    "highCount": {highcount}
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
