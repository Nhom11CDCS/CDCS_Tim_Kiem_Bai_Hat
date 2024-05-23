from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")  
def check_conn():
    if es.ping():
        print("Connected to Elasticsearch!")
    else:
        print("Could not connect to Elasticsearch.")

def tim_kiem_theo_ten(name):
    query = {
        "query": {
            "match": {
                "song_name": name
            }
        }
    }
    result = es.search(index="songs_index", body=query)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            song_info = hit['_source']
            #print("Tên bài hát:", song_info.get('song_name'))
            #print("Tác giả:", song_info.get('artist'))
            #print("Lời bài hát:", song_info.get('lyrics'))
            #print("-------------------------------------")
            print(song_info)
    else:
        return False

def tim_theo_tac_gia(name):
    query = {
        "query": {
            "match": {
                "artist": name
            }
        }
    }
    result = es.search(index="songs_index", body=query)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            song_info = hit['_source']
            #print("Tên bài hát:", song_info.get('song_name'))
            #print("Tác giả:", song_info.get('artist'))
            #print("Lời bài hát:", song_info.get('lyrics'))
            #print("-------------------------------------")
            print(song_info)
    else:
        print("Không tìm thấy bài hát nào có tên:", name)

def tim_theo_lyric(lyric):
    query = {
        "query": {
            "match": {
                "lyrics": {
                    "query": lyric,
                    "fuzziness": "AUTO"
                }
            }
        }
    }
    result = es.search(index="songs_index", body=query)
    hits = result['hits']['hits']
    if hits:
        for hit in hits:
            song_info = hit['_source']
            #print("Tên bài hát:", song_info.get('song_name'))
            #print("Tác giả:", song_info.get('artist'))
            #print("Lời bài hát:", song_info.get('lyrics'))
            #print("-------------------------------------")
            print(song_info)
    else:
        print("Không tìm thấy bài hát nào có lyric:", name)

def them_ban_ghi(name, artist, lyric):
    if not tim_kiem_theo_ten:
        print("already exist")
    song_record = {
        "song_name": name,
        "artist": artist,
        "lyrics": lyric
    }
    response = es.index(index="songs_index", body=song_record)
    print(response.get('result')) 

def chinh_sua(doc_id,new_name, new_artist, new_lyric):
    update_body = {
        "doc": {
            "song_name": new_name,
            "artist": new_artist,
            "lyric": new_lyric
        }
    }
    response = es.update(index="songs_index", id=doc_id, body=update_body)
    print(response)
    

def xoa(doc_id): 
    response = es.delete(index="songs_index", id=doc_id)    
    print(response)






#check_conn()
#tim_kiem_theo_ten("chuc be ngu ngo")
#tim_theo_tac_gia("be xuan mai")
#tim_theo_lyric("dem da khuya roi")
txt="Đoàn quân Việt Nam đi chung lòng cứu quốc, bước chân dồn vang trên đường gập ghềnh xa, cờ in máu chiến thắng mang hồn nước, súng ngoài xa chen khúc quân hành ca, đường vinh quang xây xác quân thù, thắng gian lao cùng nhau lập chiến khu, vì nhân dân chiến đấu không ngừng, tiến mau ra sa trường. Tiến lên, cùng tiến lên, nước non Việt Nam ta vững bền.Đoàn quân Việt Nam đi, sao vàng phấp phới. Dắt giống nòi quê hương qua nơi lầm lan. Cùng chung sức phấn đấu xây đời mới. Đứng đều lên gông xích ta đập tan. Từ bao lâu ta nuốt căm hờn. quyết hy sinh đời ta tươi thăm hơn. Vì nhân dân chiến đấu không ngừng. tiến mau ra sa trường. tiến lên cùng tiến lên Nước non Việt Nam ta vững bền."
them_ban_ghi("em cua ngay mai", "son tung",txt)