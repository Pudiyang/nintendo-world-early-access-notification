
This Python script helps you to get notified when the Nintendoworld early access ticket is available. You can follow the below steps to use it:

1. Download the code and install the required packages using pip. Run the following command in your terminal:
    
    ```pip3 install -r requirements.txt```
    
2. Open the `config.ini` file and replace the `SENDER_EMAIL`, `RECEIVER_EMAILS` and `SENDER_PASSWORD` fields with your email address and password.
3. Update the `TICKET_DATE` field with the date you want to monitor.
4. Update the `COOKIE_STRING` field with the cookie from the `PurchaseTicket.aspx` request header of the Universal selection Nintendo EA date process. You can copy and paste the entire cookie string into the `COOKIE_STRING` field. See image below.

![image](https://user-images.githubusercontent.com/36856247/226511454-226dafeb-5af1-4ec6-9710-454313438017.png)

5. Finally, run the script using the following command:
    
    ```python main.py```
    

That's it! You will now receive a notification when the early access ticket is available.
