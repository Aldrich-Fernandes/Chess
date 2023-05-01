class Movement:
    @staticmethod
    def BasicMove(Type, colour, TestVector, TrueVector, PawnFirstMove=False, PawnAttacking=False): # Pawn, King, Horse
        if Type == "P":
            if colour == "White":
                movelist = [(0,-75)]
            else: 
                movelist = [(0,75)]
            
            if PawnFirstMove:
                movelist.append(tuple(map(lambda x : x*2 ,movelist[0])))
            elif PawnAttacking:
                if colour == "White":
                    movelist.extend([(75, -75), (-75, -75)])
                else:
                    movelist.extend([(-75, 75), (75, 75)])

            if TrueVector in movelist:
                return True # Add kill move later when bothered
        elif Type == "K":
            movelist = [(75,75), (75,0), (0, 75)]
            if TestVector in movelist:
                return True
        elif Type == "H":
            movelist = [(75,150), (150, 75)]
            if TestVector in movelist:
                return True
        
        return False

    @staticmethod
    def StraightMove(TestVector):  #Rook, Queen
        if TestVector[0] == 0 or TestVector[1] == 0:
            return True              
        
        return False

    @staticmethod
    def DiagonalMove(TestVector): # Bishop, Queen
        if TestVector[0] == TestVector[1]:
            return True
        
        return False
        