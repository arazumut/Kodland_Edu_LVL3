<img width="601" alt="Ekran Resmi 2024-12-16 12 55 51" src="https://github.com/user-attachments/assets/7071bba6-0c25-464e-9e55-dc8d3d6d1154" /># Discord Görev Yönetim Botu

Bu proje, küçük ekiplerde görevleri yönetmeye yardımcı olacak bir Discord botudur. Bot, görev ekleme, silme, görüntüleme ve tamamlama yeteneklerine sahiptir. Tüm veriler bir SQLite veritabanında saklanır.

## Kurulum

1. Bu projeyi klonlayın:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```sh
    pip install -r requirements.txt
    ```

    <img width="601" alt="Ekran Resmi 2024-12-16 12 55 51" src="https://github.com/user-attachments/assets/b80cda18-b1e5-4c99-98bd-74cc8dd421db" />

3. [bot.py](http://_vscodecontentref_/7) dosyasındaki [bot.run("Your Bot Token")](http://_vscodecontentref_/8) satırında `Your Bot Token` kısmını kendi Discord bot tokeniniz ile değiştirin.

## Kullanım

Botu başlatmak için:
```sh
windows
python bot.py

mac
python3 bot.py



