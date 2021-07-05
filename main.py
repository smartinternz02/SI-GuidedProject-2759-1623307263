import os
import fileinput
import sys
import cv2
import numpy as np

def abort():
    CHOICE = int(input('Enter 98 to continue or 99 to exit: ')) == 98
    menuDisplay() if CHOICE else sys.exit()


def menuDisplay():
    print("\n-->Welcome to Inventory management menu<--\n")
    print("(1) add new item")
    print("(2) remove item")
    print("(3) print list")
    print("(4) exit")
    CHOICE = int(input("Enter user choice : "))
    menuSelection(CHOICE)


def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        printInventory()
    elif CHOICE != 4:
        print("EXIT")
        menuDisplay()
    sys.exit()


def addInventory():
    print("scan your qr code when the camera asks")
    print("Adding Inventory")
    print("================")

    def video_reader():
        cam = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cam.read()
            data, bbox, _ = detector.detectAndDecode(img)
            if data:
                print(data)
                with open('Inventory.txt', 'a') as f:
                    f.write(data + '*\n')
                break
            cv2.imshow("img", img)
            if cv2.waitKey(1) == ord("Q"):
                break
        cam.release()
        cv2.destroyAllWindows()
    video_reader()
    abort()


def removeInventory():
    print("Removing Inventory")
    print("==================")

    def video_reader():
        cam = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cam.read()
            data, bbox, _ = detector.detectAndDecode(img)
            if data:
                print(data)
                with open('Inventory.txt', 'r') as f:
                    file = f.read()
                file = list(file.split("*\n"))
                file.remove(data)
                with open('Inventory.txt', 'w') as f:
                    f.truncate()
                    f.write("*\n".join(file))
                break
            cv2.imshow("img", img)
            if cv2.waitKey(1) == ord("Q"):
                break
        cam.release()
        cv2.destroyAllWindows()
    video_reader()
    abort()


def printInventory():
    with open('Inventory.txt', 'r') as f:
        InventoryFile = f.read()
    InventoryFile = list(InventoryFile.split("*\n"))
    print('Current Inventory')
    print('-----------------')
    for item in InventoryFile:
        if item != '':
            item_description, item_quantity = item.rstrip("\n").split("\n")
            print('Item:     ', item_description)
            print('Quantity: ', item_quantity.rstrip("*"))
            print('----------')
    abort()





menuDisplay()








