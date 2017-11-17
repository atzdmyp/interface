from matplotlib import pyplot as plt
import readConfig as readConfig

x=[5,6,7,8]
y=[7,3,8,3]

x1=[2,4,3,9]
y1=[5,3,2,7]


def DrawLine():
    """
    绘制线用plot
    :return:
    """
    plt.plot(x,y,marker='*',color='g',linewidth=1,label='Line one')
    plt.plot(x1,y1,marker='o',color='r',linewidth=1,label='Line two')


def DrawPoints():
    """
    绘制散点图用scatter
    :return:
    """
    plt.scatter(x,y,color='g',label='Line one')
    plt.scatter(x1,y1,color='r',label='Line two')


def drawBar():
    """
    绘制柱状图用bar
    :return:
    """
    plt.bar(x, y, color='g', label='Line one')
    plt.bar(x1, y1, color='r', label='Line two')


def SetMsg():
    plt.title('Epic Chart')
    plt.xlabel('X Label')
    plt.ylabel('Y Label')


def ShowPicture():
    # 显示图例
    plt.legend()

    # 显示网格
    # plt.grid(True, color='k')

    plt.show()
    # 保存绘制的图片
    # plt.savefig(r"F:\aaaa.png")


def DrawPie():
    """
    绘制饼图用pie
    :return:
    """
    labels = 'OK', 'NG'
    fracs = [23, 1]
    colors = ['green','red']
    explode = [0, 0]  # 0.1 凸出这部分，
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    # autopct ，show percet
    plt.pie(x=fracs, colors=colors, labels=labels, explode=explode, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6
            )
    # plt.show()
    # 显示图例
    plt.legend()
    plt.savefig(r"F:\aaaa.png")
    '''
    labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    shadow，饼是否有阴影
    startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    pctdistance，百分比的text离圆心的距离
    patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
    '''

if __name__ == "__main__":
    DrawPie()
    #DrawLine()
    #SetMsg()
    ShowPicture()
    #print(CrawlPie.__doc__)
