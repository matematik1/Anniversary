[![Latest release](https://img.shields.io/badge/Release-click-labelColor=0000&logoColor=0eff0e)](https://github.com/matematik1/Anniversary/releases/latest)

# Ukrainian language
# Вітальна Листівка "З Ювілеєм!"  

Це десктопний додаток на Python, створений за допомогою Tkinter, який слугує цифровою вітальною листівкою з нагоди ювілею. Він поєднує в собі візуальні елементи, фонову музику та інтерактивні кнопки для створення персоналізованого привітання.

## 🌟 Особливості

* **Графічний інтерфейс:** Створений за допомогою Tkinter.
* **Фонова музика:** Автоматично відтворює музичний файл (`musick/musick.mp3`) при запуску.
* **Динамічна зміна зображень:** У центральній частині вікна відображаються зображення, які змінюються кожні 1.3 секунди.
* **Статичні зображення:** Використовує фонове зображення та інші декоративні елементи.
* **Вітальний текст:** Відображає віршоване привітання.
* **Інтерактивні кнопки:**
    * Кнопка для переходу на Telegram-канал.
    * Кнопка для переходу на TikTok-профіль.
    * Кнопка для переходу на GitHub-профіль.
* **Спеціальне вікно закриття:** При спробі закрити вікно з'являється діалогове вікно з прощальним повідомленням.
* **Фіксований розмір вікна:** Вікно має розмір 963x766 пікселів і не може бути змінене.
* **Вікно поверх інших:** Додаток завжди відображається поверх інших вікон.
* **Іконка додатку:** Має власну іконку.

## 🛠️ Використані технології та бібліотеки

* **Python 3**
* **Tkinter:** Для створення графічного інтерфейсу користувача.
* **Pygame (mixer):** Для відтворення фонової музики.
* **Pillow (PIL):** Для роботи із зображеннями (завантаження та відображення).
* **webbrowser:** Для відкриття URL-адрес у веб-браузері.
* **itertools:** Використовується у класі `ImageLabel`.
* **random:** Для випадкового вибору зображень.

## 🚀 Як запустити

1.  **Клонуйте репозиторій:**
    ```bash
    git clone <URL-вашого-репозиторію>
    cd <назва-папки-репозиторію>
    ```

2.  **Встановіть необхідні бібліотеки:**
    ```bash
    pip install pygame Pillow
    ```
    (Tkinter зазвичай входить до стандартної бібліотеки Python).

3.  **Переконайтеся, що файли знаходяться у правильних директоріях:**
    * Музичний файл: `musick/musick.mp3`
    * Іконка додатку: `image/app.ico`
    * Зображення для кнопок: `image/tg.png`, `image/tt.png`, `image/git.png`
    * Фонове зображення: `image/font1.png`
    * Декоративні зображення: `image/used.png`, `image/anniversary.png`
    * Зображення для слайд-шоу (25 файлів): `image/img (1).png`, `image/img (2).png`, ..., `image/img (25).png`

4.  **Запустіть скрипт:**
    ```bash
    python <назва_вашого_файлу.py>
    ```

## 📂 Структура файлів та папок (очікувана)
.
├── <назва_вашого_файлу.py>    # Основний скрипт Python

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

## 📝 Можливі доопрацювання та налаштування

* **Зміна музики:** Замініть файл `musick/musick.mp3` на власний.
* **Зміна зображень:**
    * Замініть файли в папці `image/` на власні, дотримуючись імен або змінивши їх у коді.
    * Кількість зображень для слайд-шоу (клас `RandomImage`) можна змінити, оновивши цикл у конструкторі класу.
* **Редагування тексту:** Змініть вітальний текст у секції `#текст` коду.
* **Зміна посилань:** Оновіть URL-адреси у функціях `open_TG()`, `open_TT()`, `open_GitHub()`.
* **Налаштування гучності:** Змініть значення змінної `nam` (від 0.0 до 1.0) для налаштування гучності музики.

## ❤️ Повідомлення при закритті

При спробі закрити додаток, користувач побачить повідомлення: "Люблю тебе😘", "Зоходь ще як небудь!".

---

Сподіваюсь, ця вітальна листівка принесе радість!

#English
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
