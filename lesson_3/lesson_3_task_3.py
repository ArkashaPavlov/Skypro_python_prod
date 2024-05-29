from Address import Address
from Mailing import Mailing

sender = Address(1111111,"Perm","Pushcina","14","88")
recipient = Address(2222222,"New-York","Colotushcina","9","11")

package = Mailing(recipient, sender, 500, "Pushcina - Colotushcina")

print("Отправление", package.track, "из", package.from_address.thisIndex,",",package.from_address.thisSyti,",",package.from_address.thisStreet,",", package.from_address.thisHouse," - ", package.to_address.thisIndex,",",package.to_address.thisSyti,",",package.to_address.thisStreet,",", package.to_address.thisHouse,". Стоимость ", package.cost, "рублесов")