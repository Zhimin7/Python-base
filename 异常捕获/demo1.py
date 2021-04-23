'''
异常捕获

格式：
try:
    可能出现异常的代码

except:
    异常处理

finally:
    不论是否异常都会执行

'''


def deviser():
    try:
        num1 = int(input('请输入第一个数字：'))
        per = input('请输入符号：（+、-、*、/）')
        num2 = int(input('请输入第二个数字：'))
        result = 0
        if per == '+':
            result = num2 + num1
        elif per == '-':
            result = num1 - num2
        elif per == '*':
            result = num2*num1
        elif per == '/':
            result = num1/num2
        # print(result)
        with open(r'D;\result.txt', 'w') as f:
            f.write(str(result))


    except ZeroDivisionError:
        print('除数不能为0')
    except ValueError:
        print('必须输入数字')
    # except Exception:
    #     pass
    except TypeError:
        print('write 方法写入的必须是字符串')
    # with open('result.txt', 'w') as f:
    #     f.write(result)

    except Exception as err:
        print('出错了', err)

deviser()
