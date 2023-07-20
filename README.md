# MessageBroker
1 Topic içerisinde 3 Partiton var. Bu senaryoya göre sırasyıla 3 consumer partitoanlara subscribe olucak. 1. consumer tm partionlara baglanarak veriyi okuayacak.
2. consumer calıştırdıgım anda ilk consumer ile roundrobin algortmasyıla birbirleri arasında partitionlara bölünecek. Örnekte 0 ve 1. partitona ilk consume subsribe oldu. 2.partiona ise 2. consume baglandı.
3. consumer ı çalıştırdıgımda yine roundrobine ile partitonlar bölüşüldü.


![image](https://github.com/omerulusoy41/MessageBroker/assets/73287349/f1a02e6a-3536-4ecc-a12f-ef74d21610c2)

