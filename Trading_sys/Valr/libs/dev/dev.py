import sys

sys.path.append("D:/work/projects/dev/projects/TurtleTurtle_v4")

import libs.utils.toolUtils as ToolUtils


def quick_calculate_profit(value):


    number = ToolUtils.percent_increase(3, value)


    return(number)




if __name__ == '__main__':

    value = 10000

    n = quick_calculate_profit(value)


    print('R', n)