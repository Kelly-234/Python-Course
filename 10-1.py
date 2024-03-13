import urllib.request
from bs4 import BeautifulSoup


def main():
    url = "https://www.shanghairanking.cn/rankings/bcur/2021"
    html = askURL(url)
    dataList = getData(html)
    printData(dataList, province)


def askURL(url):
    head = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
        "Cookie":
        "UM_distinctid=172472406747c7-0848d98601b4ba-d373666-144000-17247240675c26; stationid=54517; ray_leech_token=1590334450; CNZZDATA1254743953=555270005-1590328798-%7C1590329122"
    }
    req = urllib.request.Request(url, headers=head)
    res = urllib.request.urlopen(req)
    html = res.read().decode()
    return html


def getData(html):
    dataList = []
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("tbody")
    tdList = table.find_all("td")
    n = len(tdList) // 6
    for i in range(n):
        tempData = []
        for j in range(5):
            tempData.append(tdList[i * 6 + j].text.strip().split(" ")[0])
        dataList.append(tempData)
    return dataList


def printData(dataList, province):
    print("{0:<4}{1:{5}^16}{2:{5}<5}{3:{5}^8}{4:{5}<10}".format(
        " 排名", " 学校名称  ", "省市", "类型", "总分", chr(12288)))
    for data in dataList:
        if data[2] == province:
            print("{0:<4}{1:{5}^14.5}{2:{5}<5}{3:{5}^8}{4:{5}<10.1f}".format(
                chr(12288) + data[0], data[1], data[2], data[3],
                float(data[4]), chr(12288)))


province = input("请输入省份名：")
main()
