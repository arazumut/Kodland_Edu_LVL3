  <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
  </a> 
    
Bu proje, Discord botu olarak çalışan bir görev yönetim sistemidir. Bot, kullanıcıların Discord üzerinden görev eklemelerine, silmelerine, görüntülemelerine ve tamamlamalarına olanak tanır. İşte projenin ana işlevleri:

Görev Ekleme: Kullanıcılar !add_task <görev açıklaması> komutunu kullanarak yeni görevler ekleyebilirler.
Görev Silme: Kullanıcılar !delete_task <görev ID> komutunu kullanarak mevcut görevleri silebilirler.
Görevleri Görüntüleme: Kullanıcılar !show_tasks komutunu kullanarak tüm görevleri listeleyebilirler.
Görev Tamamlama: Kullanıcılar !complete_task <görev ID> komutunu kullanarak görevleri tamamlanmış olarak işaretleyebilirler.
Bot, SQLite veritabanı kullanarak görevleri saklar ve yönetir. Botun çalışması için bir Discord bot tokenine ihtiyaç vardır.
