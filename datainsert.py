from neo4j import GraphDatabase, BoltStatementResult

class datainsert(object):

    def __init__(self):
        self._driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","TYU9kat9"))

    def close(self):
        self._driver.close()

    def create_person(self, name):
        with self._driver.session() as session:
            session.run("MERGE (person:Person {name:$name}) ", name=name)

    def rel(self, name, name2, node,node2,r):
        with self._driver.session() as session:
            session.run('MATCH (a:%s {name:"%s"}) '%(node,name) +
                        'MERGE (b:%s {name:"%s"}) '%(node2,name2) +
                        'MERGE (a) -[r:%s]-> (b) ' %(r))


    def ruijikensaku(self, name):
        with self._driver.session() as session:
            r=session.run('MATCH (p:Parson) ' +
                            'WHERE p.name =~ ".*%s.*"'%(name) +
                            'RETURN p' )

        return r



class question():

    def __init__(self):
        self.you=""
        self.hobby=""

    def person(self):
        print("あなた誰？\n>")
        self.set_your_name(input_totonoe())

        q_data=datainsert()
        q_data.create_person(self.you)
        tmp=q_data.ruijikensaku(self.you)
        for i in tmp:
            print(i)
        q_data.close()

    def set_your_name(self,name):
        self.you=name


    def hobby(self):
        print("趣味は？")



def input_totonoe():
    s=input()
    s=s.replace(" ","")
    s=s.replace("　","")
    return s

if __name__ == '__main__':

    friend_list=["野崎裕人", "松本芳樹", "小坂恭平" ,"石原裕介"]
    hobby_list={"ゲーム","動画鑑賞","Vtuber"}

    data=datainsert()


    data.create_person("平林克秀")
    for i in friend_list:
        data.rel("平林克秀",i,"Person","Person","友達")
    for i in hobby_list:
        data.rel("平林克秀",i,"Person","Hobby","趣味")
    data.close()
    q=question()
    q.person()






