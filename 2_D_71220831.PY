def cetakHuruf () :
    huruf=(input("Masukkan kata :"))
    list=(huruf)
    len(huruf)
    if(len(huruf)%2==0) :
        print("huruf paling ujung pada huruf", huruf, "adalah", (huruf[-3:]))
    else :
        print("huruf paling ujung pada huruf", huruf, "adalah",(huruf[:3]))
    return (huruf)
cetakHuruf()