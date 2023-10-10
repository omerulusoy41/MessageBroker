# MessageBroker
- 1 Topic içerisinde 3 Partiton var. Bu senaryoya göre sırasyıla 3 consumer partitoanlara subscribe olucak. 1. consumer tm partionlara baglanarak veriyi okuayacak.
2. consumer calıştırdıgım anda ilk consumer ile roundrobin algortmasyıla birbirleri arasında partitionlara bölünecek. Örnekte 0 ve 1. partitona ilk consume subsribe oldu. 2.partiona ise 2. consume baglandı.
3. consumer ı çalıştırdıgımda yine roundrobine ile partitonlar bölüşüldü.


![image](https://github.com/omerulusoy41/MessageBroker/assets/73287349/f1a02e6a-3536-4ecc-a12f-ef74d21610c2)

- Topic üzerindeki verilerin tekarar tekrar okunmması için okumayı hemr latest yaptım hemde okunan verileri commit ettim
![image](https://github.com/omerulusoy41/MessageBroker/assets/73287349/4a145c53-27b6-41cd-800c-4bdb7c0aca7a)
- farklı consumer grouplar bu durumdan etkilenmez. Eski Verileri de okur.
- ![image](https://github.com/omerulusoy41/MessageBroker/assets/73287349/05b68add-e757-4143-97c5-17094a0b39c1)



