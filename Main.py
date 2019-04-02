from selenium import webdriver
import time
import Mail_sender as Ms
import Screenshot as Ss


def shape():
    driver = webdriver.Chrome()
    driver.get('https://www.kauppalehti.fi/porssi/porssikurssit/osake/NIXU')
    Ss.take_shot('screen')
    time.sleep(0.5)
    element_x = ""
    try:
        try:
            element_x = driver.find_element_by_css_selector("div[class='indicecard stock-card-index odd']")
        except:
            element_x = driver.find_element_by_css_selector("span[class='changePercent indicecardRow change-negative']")
    except:
        driver.quit()
        Ms.send_message('valtteri.salmijarvi@jyno.fi', "Nixu sender", "!Connection error!", 'screen.png')
        print("You are not connected to internet")
        exit(81)

    x = element_x.text
    driver.quit()
    charters = ['']
    text1 = ['']

    text1 = list(x)

    for i in range(0, len(x)):
        if text1[i] == "u":
            charters.append("u ")
        elif text1[i] == "%":
            charters.append("%\n")
        elif text1[i] == "R":
            charters.append("R\nAika: ")
        else:
            charters.append(text1[i])

    out = ''.join(charters)
    return out


def main():
    for i in range(0, 24):
        percent = shape()
        print(percent)
        Ms.send_message('valtteri.salmijarvi@jyno.fi', "Nixu oy (" + time.strftime("%H:%M") + ')', percent,
                        'screen.png')
        time.sleep(10)


if __name__ == '__main__':
    main()
