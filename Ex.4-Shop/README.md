Stworzenie implementacji systemu
obsługi faktur, opartego na repozytorium.
Rozszerzyć ją o magazyn produktów, który podobnie jak 
repozytorium faktur będzie parametrem konstrukcji sklepu. 
Magazyn powinien posiadać wiedzę o dostęnych produktach, ich ilościach i cenach.
Dodatkowo powinien oferować operacje przyjęcia na magazym oraz wydania z magazynu.
Próba wydania z magazynu produktu o zerowym stanie mgazynowym powinna 
generować wyjątek `OutOfStore`. 
W sklepie powinna być dostępna operacja zwrotu częściowego towarów z danej
faktury.

Każda sprzedaż oraz zwrot prócz repozytorium faktur zmieniają również 
stany magazynowe.


Wykorzystując koncepcję różnych *test double*, przetestować czy odpowiednie
operacje z klasy `Shop` w zależności od parametrów oraz stanu repozytorium 
faktur i magazynu:
- uruchamiają odpowiednie metody z obu ww. w odpowiedniej liczbie 
  i z odpowiednimi parametrami
  
- czy opracje te dają odpowiedni wynik

Do realizacji testów użyj *test double (stub, dummy, fake, spy oraz mock)* 
o odpowiedniej funkcjonalności.