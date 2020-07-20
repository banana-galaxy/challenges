def lateRide(minutes):
  return((minutes%60)%10+(minutes%60)//10+(minutes//60)%10+(minutes//60)//10)