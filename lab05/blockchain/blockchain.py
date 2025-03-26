from block import Block
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []  # Danh sách lưu trữ các block
        self.current_transactions = []  # Danh sách giao dịch tạm thời
        self.create_block(proof=1, previous_hash="0")  # Tạo block khởi nguyên (Genesis Block)

    def create_block(self, proof, previous_hash):
        """Tạo một block mới và thêm vào chuỗi"""
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []  # Reset giao dịch sau khi tạo block
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """Lấy block cuối cùng trong chuỗi"""
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """Thuật toán Proof of Work để tìm proof hợp lệ"""
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Điều kiện khó khăn của blockchain
                check_proof = True
            else:
                new_proof += 1       
        return new_proof
    
    def add_transaction(self, sender, receiver, amount):
        """Thêm giao dịch mới vào danh sách giao dịch"""
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.get_previous_block().index + 1  # Trả về chỉ số của block sẽ chứa giao dịch

    def is_chain_valid(self, chain):
        """Kiểm tra tính hợp lệ của blockchain"""
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            # Kiểm tra hash của block hiện tại có trùng với previous_hash của block tiếp theo không
            if block.previous_hash != previous_block.hash:
                return False

            # Kiểm tra proof của block
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4] != "0000":  # Điều kiện PoW không thỏa mãn
                return False

            previous_block = block
            block_index += 1
        
        return True