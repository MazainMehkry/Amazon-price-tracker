This is an Amazon Price Tracker, which i made for my personal use. Currently it works for Amazon.in(India) and Amazon.ae(UAE).

I recently learned python programming and decided to put it to use. I used tkinter, customtkinter and soup for this project.
If there is anyway i can improve it, please feel free to let me know here - mazain.k@gmail.com

![Front UI](https://user-images.githubusercontent.com/87644146/221402447-b6eddac5-678a-4409-aee2-192aefb58125.png)

This is the front UI of the project, you need to enter an amazon product link and an expected price (do not make it unrealistic) under which you want the product for.

If you do not enter correct amazon link or do not enter integer value, you will get a warning.

![Does not exist](https://user-images.githubusercontent.com/87644146/221403506-d299e670-f0e3-494a-aff8-201d46aa14f4.png)

![Rubbish instead of price](https://user-images.githubusercontent.com/87644146/221403513-89716abc-5fec-4b14-8ef8-ed6f8f6999cc.png)

After entering correct link and price, you have to click on "add" button. 

![Added finally](https://user-images.githubusercontent.com/87644146/221403585-9371f709-d5f9-4c1b-9317-f01d37e35498.png)

After you add few products link and price. You can click on "check" button, which will go through each link and compare the price. If any product is currently under
your given price then you will get a popup with the details of the product one by one.

![Item on sale and will be copied](https://user-images.githubusercontent.com/87644146/221403678-bd93a399-d767-4c16-b1be-c0f09ed33136.png)

The link of the product will also be copied to your clipboard after you click on "ok", so make sure to open any browser and paste the link before clicking on next "ok".

![want to delete after getting it on sale](https://user-images.githubusercontent.com/87644146/221403809-114738b4-be78-4d5c-9b7b-7e2e39afe76d.png)

After you click on "Ok", you will get the above pop up. You can either choose to delete the link and price or keep it. 

After going through each link, if there were one or more product on sale, you will get the following:

![Item on sale and end](https://user-images.githubusercontent.com/87644146/221403934-8b183ead-e2dc-4efb-989c-16da2c9f98ac.png)

And if there were no items on sale, you will get the following:

![No item on sale and end](https://user-images.githubusercontent.com/87644146/221403945-e4ff80d2-345f-4a2f-8097-e295725c3d24.png)

If you want to delete everything, you can click on the "delete" button to clear everything.

![delete](https://user-images.githubusercontent.com/87644146/221404034-b3ef3f5c-8f58-43aa-83fc-2a49015b27e8.png)


Other Notes:
  - If you do not enter a link or price, you will get a warning respectively.
  - If an item is currently out of stock, you will get a popup informing you of it after you click on the "check" button.
  - If you click on "check" button without actually entering any details, you will get a warning.
  - If you click on "delete" button when it is already empty, you will get a warning.
  - If you try to enter the same link again, you will get a warning.
  
  
  
