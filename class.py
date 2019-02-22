import sys, re
  

def second_element(x):
  return x[1]

def helper(filename):
  with open(filename, 'r') as f:
    words = f.read().split()

  rd = dict()  
  for word in words:
    rd[word]=words.count(word)
    
  return rd

def print_words(filename):
  target = helper(filename)  
  for t1,t2 in target.items():
    print t1, t2

def print_top(filename):
  target = helper(filename)
  res = target.items()
  res.sort(key=second_element, reverse=True)
  top = list()
  p = 0
  for t1,t2 in res:
    if p == 20:
      break
    else:
      top.append((t1,t2))
      p = p + 1

  top.sort(key=lambda x: x[0])
  for t1,t2 in top:
    print t1

# print_words(filename)�� print_top(filename) �Լ��� �ۼ��ϼ���
# ������ ����, �ܾ ���� dict�� ��ȯ�ϴ� ���� �Լ��� �����ص� �˴ϴ�
# print_words �Լ��� print_top �Լ����� ���� �Լ��� ȣ���ϸ� �˴ϴ�

###

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
