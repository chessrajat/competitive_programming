'''
/*
 * @Author: Rajat  
 * @Date: 2021-01-03 13:33:29 
 * @Last Modified by: Rajat
 * @Last Modified time: 2021-01-03 13:47:43
 */
'''
def gradingStudents(grades):
    # Write your code here
    response = []
    for grade in grades:
        result = abs((grade % 5) -5)
        if(result < 3):
            res = grade + result
            if res < 40:
                response.append(grade)
            else:
                response.append(res)
        else:
            response.append(grade)
    return response

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)