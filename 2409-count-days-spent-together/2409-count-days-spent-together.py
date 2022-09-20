class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        alice_day1=sum(days[:int(arriveAlice[:2])-1])+int(arriveAlice[3:])
        alice_day2=sum(days[:int(leaveAlice[:2])-1])+int(leaveAlice[3:])
                      
        bob_day1=sum(days[:int(arriveBob[:2])-1])+int(arriveBob[3:])
        bob_day2=sum(days[:int(leaveBob[:2])-1])+int(leaveBob[3:])
  
        return max(0,min(alice_day2,bob_day2)-max(bob_day1,alice_day1)+1)

        
        