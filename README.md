Sau khi đã tải hai file của challenge, một file code và một file text. Mở file text ta sẽ có hai số a, b và một tupple ciphertext, ciphertext dạng array có nghĩa là đây là dạng mã hóa từng kí tự.

Tiếp theo ta sẽ thực hiện đọc code của file encrypt để biết được cách mà chương trình mã hóa dữ liệu nhằm tìm ra plaintext cũng chính là flag của challenge.

Source code sẽ có một số hàm quan trọng sau đây:

def generator(g, x, p):
    return pow(g, x) % p

->hàm này sẽ tính g mũ x mod p

def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher

-> hàm này sẽ encrypt từng kí tự của plaintext bằng cách lấy giá trị dec của kí tự đem nhân cho key cùng với 311, mỗi giá trị sẽ được lưu thành từng phần tử trong array cipher

def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

-> hàm này sẽ thực hiện việc đảo ngược lại plaintext, sau đó sẽ đem xor từng kí tự của plaintext với từng kí tự của key để thu được ciphertext

def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')

-> đây là hàm quan trọng để thực hiện việc mã hóa plaintext, đầu tiên chương trình sẽ thực thi thuật toán deffine-hellman để trao đổi khóa, ta sẽ thu được khóa share_key dùng cho việc mã hóa sau này.
Phần tiếp theo vô cùng quan trọng, chú ý hai biến là semi_cipher và cipher, semi_cipher sẽ thực hiện mã hóa plaintext bằng hàm dynamic_xor_encrypt bằng khóa text_key chính là "trudeau" ở dòng cuối của source code.
cipher sẽ thực hiện việc mã hóa tiếp tục semi_cipher bằng khóa shared_key, cuối cùng thu được ciphertext.

Bây giờ để tìm được plaintext ta chỉ cần làm ngược lại, ý tưởng sẽ là như thế này:
Việc mã hóa sẽ là: plaintext -> dynamic_xor_encrypt -> encrypt -> ciphertext, nên việc giải mã sẽ là: ciphertext -> decrypt -> decrypt_xor -> plaintext với decrypt là làm ngược lại encrypt, decrypt_xor là làm ngược lại dynamic_xor_encrypt.
Việc tìm share_key cũng quan trọng trong việc tìm plaintext vì nó sẽ được dùng trong hàm decrypt (vì hàm encrypt cũng dùng khóa này để mã hóa), vì ta đã có p = 97, g = 31 (theo source code) và a = 95, b = 21 (theo flag_infor), khóa này được tạo theo thuật toán deffine_hellman, bạn có thể tìm hiểu thêm 

Mình đã giải thích luồng xử lý để giải mã, tiếp theo phần source code giải mã mình sẽ up bằng file python nhé!
