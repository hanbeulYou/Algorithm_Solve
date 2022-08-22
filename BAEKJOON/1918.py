# p1_후위 표기법(extra)
# 2022-08-22

# 들어온 문자에 따른 우선순위 판단
def primary(char):
    if char == '(':
        return 3
    elif char == '*' or char == '/':
        return 2
    elif char == '+' or char =='-':
        return 1
    else:
        return 0

operator = ['+', '-', '*', '/']
expression = list(input())
stack = []
stack_len = 0

for element in expression:
    # 괄호(열린) 처리
    if element == '(':
        stack.append(element)
        stack_len += 1
    # 괄호(닫힌) 처리
    elif element == ')':
        # 괄호가 열린 위치 위에 쌓인 요소 모두 pop
        while stack_len > 0:
            if stack[stack_len-1] == '(':
                stack.pop()
                stack_len -= 1
                break
            else:
                print(stack.pop(), end='')
                stack_len -= 1
        
    # 연산자 처리
    elif element in operator:
        # 최대로 스택이 모두 비워질 때까지 확인
        while stack_len > 0:
            # 만약 top의 우선 순위가 현재 연산자보다 낮을 때
            if primary(stack[-1]) < primary(element):
                break
            # 만약 top이 괄호일 때
            elif stack[-1] == '(':
                break
            # top 요소의 우선 순위가 현재 연산자보다 낮거나 같을 때
            # pop 해버림
            else:
                print(stack.pop(), end='')
                stack_len -= 1
        # 연산자 처리 후 새 요소 append
        stack.append(element)
        stack_len += 1
    
    # 숫자 처리
    else :
        print(element, end='')

# stack에 남아있는 요소들 처리
while stack :
    print(stack.pop(), end='')