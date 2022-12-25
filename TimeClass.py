class Time:
    def __init__(self,hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

    def sum(self, other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour   + other.hour
    
        r = Time(h_new,m_new,s_new)
        return r

    def sub(self, other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour

        r = Time(h_new, m_new, s_new)
        return r

    def sec2t(self):
        s = int(input('Enter seconds: '))
        hh = s//3600
        mm = (s%3600)/60
        ss = ((s%3600)%60)
        x = Time(hh,mm,ss)
        return x

    def t2sec(self):
        x = self.second + self.minute*60 + self.hour*3600
        print(x)
        return x

    def GMT2Teh(self):
        Teh = Time(3,30,0)
        x = Time.sum(Teh,self)
        return x
    
t1 = Time(3,45,17)
t1.show()

t2 = Time(4,13,2)
t2.show()

t3 = t1.sum(t2)
t3.show()