[![Latest release](https://img.shields.io/badge/Release-click-labelColor=0000&logoColor=0eff0e)](https://github.com/matematik1/Anniversary/releases/latest)

# Anniversary Greeting Card!

This is a desktop application in Python, created using Tkinter, which serves as a digital greeting card for an anniversary. It combines visual elements, background music, and interactive buttons to create a personalized greeting.

## 🌟 Features

* **Graphical Interface:** Built with Tkinter.
* **Background Music:** Automatically plays a music file (`musick/musick.mp3`) upon launch.
* **Dynamic Image Slideshow:** Images are displayed in the central part of the window and change every 1.3 seconds.
* **Static Images:** Uses a background image and other decorative elements.
* **Greeting Text:** Displays a poetic greeting.
* **Interactive Buttons:**
    * Button to navigate to a Telegram channel.
    * Button to navigate to a TikTok profile.
    * Button to navigate to a GitHub profile.
* **Custom Closing Window:** When attempting to close the window, a dialog box appears with a farewell message.
* **Fixed Window Size:** The window has a size of 963x766 pixels and cannot be resized.
* **Always on Top:** The application window is always displayed above other windows.
* **Application Icon:** Has its own custom icon.

## 🛠️ Technologies and Libraries Used

* **Python 3**
* **Tkinter:** For creating the graphical user interface.
* **Pygame (mixer):** For playing background music.
* **Pillow (PIL):** For working with images (loading and displaying).
* **webbrowser:** For opening URLs in a web browser.
* **itertools:** Used in the `ImageLabel` class.
* **random:** For random selection of images.

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-URL>
    cd <repository-folder-name>
    ```

2.  **Install the necessary libraries:**
    ```bash
    pip install pygame Pillow
    ```
    (Tkinter is usually included in the standard Python library).

3.  **Ensure the files are in the correct directories:**
    * Music file: `musick/musick.mp3`
    * Application icon: `image/app.ico`
    * Button images: `image/tg.png`, `image/tt.png`, `image/git.png`
    * Background image: `image/font1.png`
    * Decorative images: `image/used.png`, `image/anniversary.png`
    * Slideshow images (25 files): `image/img (1).png`, `image/img (2).png`, ..., `image/img (25).png`

4.  **Run the script:**
    ```bash
    python <your_script_name.py>
    ```

## 📂 File and Folder Structure (Expected)
.
├── <your_script_name.py>    # Main Python script

├── image/

│   ├── app.ico

│   ├── anniversary.png

│   ├── font1.png

│   ├── git.png

│   ├── img (1).png

│   ├── ...

│   ├── img (25).png

│   ├── tg.png

│   ├── tt.png

│   └── used.png

└── musick/

└── musick.mp3

## 📝 Possible Enhancements and Customizations

* **Change Music:** Replace the `musick/musick.mp3` file with your own.
* **Change Images:**
    * Replace files in the `image/` folder with your own, keeping the names or changing them in the code.
    * The number of images for the slideshow (class `RandomImage`) can be changed by updating the loop in the class constructor.
* **Edit Text:** Change the greeting text in the `#текст` (text) section of the code.
* **Change Links:** Update the URLs in the `open_TG()`, `open_TT()`, and `open_GitHub()` functions.
* **Adjust Volume:** Change the value of the `nam` variable (from 0.0 to 1.0) to adjust the music volume.

## ❤️ Closing Message

When trying to close the application, the user will see the message: "Люблю тебе😘", "Зоходь ще як небудь!" (I love you😘, Come back again sometime!).

---

Hope this greeting card brings joy!
