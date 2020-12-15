# Tranforms path into orders to be sent to the robot

def encoder(arr):
    instr=[]
    cont=0
    mov=[0,0]
    orient='AR'

    for i in range(len(arr)-1):

     mov[0]=arr[i+1][0]-arr[i][0]
     mov[1]=arr[i+1][1]-arr[i][1]
     if mov[0]>0:
        if orient=='D':
          instr.append('GI')

        if orient=='I':
          instr.append('GD')

        if orient=='AB':
           instr.append('GD')
           instr.append('GD')


        instr.append('A'+ str(mov[0]))
        orient='AR'
     if mov[0]<0:
        if orient=='D':
         instr.append('GD')

        if orient=='I':
          instr.append('GI')

        if orient=='AR':
           instr.append('GD')

           instr.append('GD')

        
        instr.append('A'+ str(-mov[0]))

        orient='AB'
     if mov[1]>0:
        if orient=='AR':
          instr.append('GD')

        if orient=='AB':
          instr.append('GI')

        if orient=='I':
           instr.append('GD')

           instr.append('GD')

        instr.append('A'+ str(mov[1]))

        orient='D'
     if mov[1]<0:
        if orient=='AR':
         instr.append('GI')

        if orient=='AB':
          instr.append('GD')

        if orient=='D':
           instr.append('GD')

           instr.append('GD')

        
        instr.append('A'+ str(-mov[1]))

        orient='I'
    
    return instr
