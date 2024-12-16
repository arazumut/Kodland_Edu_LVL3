# Discord Görev Yönetim Botu

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

3. [bot.py](http://_vscodecontentref_/7) dosyasındaki [bot.run("Your Bot Token")](http://_vscodecontentref_/8) satırında `Your Bot Token` kısmını kendi Discord bot tokeniniz ile değiştirin.

## Kullanım

Botu başlatmak için:
```sh
python bot.py