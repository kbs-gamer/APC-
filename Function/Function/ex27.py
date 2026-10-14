def hospital_bill(consultation, lab, medicine, room):
    total = consultation + lab + medicine + room

    discount = total * 0.10

    final_bill = total - discount

    return final_bill


consultation = float(input("Consultation charges: "))
lab = float(input("Laboratory charges: "))
medicine = float(input("Medicine charges: "))
room = float(input("Room charges: "))

print("Final Hospital Bill =", hospital_bill(
    consultation, lab, medicine, room
))