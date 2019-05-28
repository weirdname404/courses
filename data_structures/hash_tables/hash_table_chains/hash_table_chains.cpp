#include <utility>
#include <iostream>

struct Chain {
    int key;
    std::string value;
    Chain *next;

    Chain() {
        key = 0;
        value = "";
        next = nullptr;
    }

    Chain(int a, const std::string &b) {
        key = a;
        value = b;
        next = nullptr;
    }

    virtual ~Chain();
};

Chain::~Chain() {
    delete next;
}

class HashTable {
    int a, b, p, cardinality, len;
    Chain **arr;

public:
    explicit HashTable(int card) {
        p = 10000019;
        a = std::rand() % p;
        b = std::rand() % p;
        arr = InitArr(card);
    }

    float getLoadFactor();

    int Hash(int key);

    void Append(int key, const std::string &value);

    void Rehash();

    Chain **InitArr(int card);

    std::string Find(int key);

    void Delete(int key);


    virtual ~HashTable();
};

HashTable::~HashTable() {
    delete[] arr;
};

int HashTable::Hash(int key) {
    int i = (((long long) a * key + b) % p) % cardinality;
//    std::cout << i << std::endl;
    return i;
}

void HashTable::Append(int key, const std::string &value) {
    auto *newChain = new Chain(key, value);

    int i = Hash(key);
    Chain *currentChain = arr[i];
    if (currentChain == nullptr) {
        arr[i] = newChain;
    } else {
        auto *prevChain = currentChain;
        while (currentChain != nullptr) {
            if (currentChain->key == key) {
                currentChain->value = value;
                delete (newChain);
                return;
            }
            prevChain = currentChain;
            currentChain = currentChain->next;
        }
        prevChain->next = newChain;
    }
    len += 1;
//    std::cout << getLoadFactor() << std::endl;

    if (getLoadFactor() > 0.5) {
        Rehash();
    }

}

std::string HashTable::Find(int key) {
    Chain *chainPtr = arr[Hash(key)];
    while (chainPtr != nullptr) {
        if (chainPtr->key == key) {
            return chainPtr->value;
        }

        chainPtr = chainPtr->next;
    }

    delete (chainPtr);

    return "not found";
}

float HashTable::getLoadFactor() {
    return float(len) / float(cardinality);
}

void HashTable::Delete(int key) {
    int i = Hash(key);
    Chain *chainPtr = arr[i];
    Chain *prevChainPtr = nullptr;

    while (chainPtr != nullptr) {
        if (chainPtr->key == key) {
            len -= 1;
            if (prevChainPtr == nullptr) {
                arr[i] = chainPtr->next;
            } else {
                prevChainPtr->next = chainPtr->next;
            }

            return;
        }
        prevChainPtr = chainPtr;
        chainPtr = chainPtr->next;
    }

    delete (chainPtr);
    delete (prevChainPtr);
}

Chain **HashTable::InitArr(int card) {
    len = 0;
    cardinality = card;
    auto **new_arr = new Chain *[card];
    for (int i = 1; i < card; i++) {
        new_arr[i] = nullptr;
    }
    return new_arr;
}

void HashTable::Rehash() {
    auto *oldArr = arr;
    auto oldCardinality = cardinality;
    arr = InitArr(cardinality * 2);

    for (int i = 0; i < oldCardinality; i++) {
        auto *chain = oldArr[i];
        while (chain != nullptr) {
            Append(chain->key, chain->value);
            chain = chain->next;
        }
    }

    delete[] oldArr;
}

int main() {
    auto ht = HashTable(10);
    std::string value, command;
    int n, key;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> command;
        if (command == "add") {
            std::cin >> key >> value;
            ht.Append(key, value);

        } else {
            std::cin >> key;
            if (command == "find") {
                std::cout << ht.Find(key) << std::endl;

            } else {
                ht.Delete(key);
            }
        }
    }

    return 0;
}