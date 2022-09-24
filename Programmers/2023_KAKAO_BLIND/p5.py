def solution(commands):
    table = dict()
    answer = []
    for i in range(1, 51):
        for j in range(1, 51):
            table[(i, j)] = [(i, j), None]
            
    for command in commands:
        # print('#')
        # for key, value in table.items():
        #     if value[1]:
        #         print(table[key])
                
        c_list = list(command.split())
        if c_list[0] == 'UPDATE':
            if len(c_list) == 4:
                for key, value in table.items():
                    if value[0] == table[(int(c_list[1]), int(c_list[2]))][0]:
                        table[key] = [value[0], c_list[3]]
            else:
                for key, value in table.items():
                    if value[1] == c_list[1]:
                        table[key] = [value[0], c_list[2]]

        if c_list[0] == 'MERGE':
            table[(int(c_list[3]), int(c_list[4]))] = [table[(int(c_list[1]), int(c_list[2]))][0], table[(int(c_list[1]), int(c_list[2]))][1]]

        if c_list[0] == 'UNMERGE':
            target = table.get((int(c_list[1]), int(c_list[2])))
            for key, value in table.items():
                if value[0] == target[0]:
                    if key == (int(c_list[1]), int(c_list[2])):
                        table[key] = ((key[0], key[1]), target[1])
                        continue
                    table[key] = [(key[0], key[1]), None]

        if c_list[0] == 'PRINT':
            if table[(int(c_list[1]), int(c_list[2]))][1]:
                answer.append(table.get((int(c_list[1]), int(c_list[2])))[1])
            else:
                answer.append('EMPTY')

    return answer

print(solution(
["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))