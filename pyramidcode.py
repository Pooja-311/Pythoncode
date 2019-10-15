from flask import Flask, request

app = Flask(__name__)

@app.route('/isPyramidWord')
def isPyramid():
    word = request.args.get('word')
    returnDict = {}
    dict = {}
    for i in word:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1

    list1 = list(dict.values())
    list1.sort()
    returnDict["isWordPyramid"] = (areConsecutive(list1,len(list1)))

    return returnDict


def areConsecutive(list1,n):
    if (list1[0] == 1):
        if (n > 1):
            result = all(i == j - 1 for i, j in zip(list1, list1[1:]))
        elif (list1[0] == 1):
            result = True
    else:
        result = False



    return result

if __name__ == '__main__':
    app.run(debug=False)

