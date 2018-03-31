import unittest
import Polynomial as pl


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.polyE = pl.Polynomial()
        self.empty_args_list = [[], ()]
        self.scalar_args_list = [ 0, 1, -1, 2, -2, 32, 16540, -47963]
        self.seq1_args_list = [ [2,17,6], [0,1,-3], [0,2,7, 0,0 ,-2], [0,0 ,-2, 3], [-2, 3, 0, 0] ]
        self.seq2_args_list = [ (2,17,6), (0,1,-3), (0,2,7, 0,0 ,-2), (0,0 ,-2, 3), (-2, 3, 0, 0) ]
        self.exception_args_list_TypeError = [ None, (1,-2,[2]),  [[],1,2], [(),1,2], (list(),-5,4), (-5,tuple(),4), (-5,(),4),(-5,4,dict()) ]
        self.exception_args_list_ValueError = [ 'a', [2,'hello',3], (-5,4,str()) ]
        self.strPoly_list = [ '2x2+17x+6', '1x-3', '2x4+7x3-2', '-2x+3', '-2x3+3x2' ]
        self.strNegPoly_list = [ '-2x2-17x-6', '-1x+3', '-2x4-7x3+2', '2x-3', '2x3-3x2' ]
        self.testMultPoly = [2,3,-1]
        self.SolutionMultPoly = [[4,40,61,1,-6],[2,-3,-10,3],[4,20,19,-7,-4,-6,2],[-4,0,11,-3],[-4,0,11,-3,0,0]]
        pass
            
    def tearDown(self):
        pass
        
    #@unittest.skip("demonstrating skipping")
    def test_init(self):
        print("test_init")
        p1 = pl.Polynomial()
        p2 = pl.Polynomial([8,-5,0,3])
        p3 = pl.Polynomial(8,-5,0,3)
        p4 = pl.Polynomial((-1,2,5))
        p5 = pl.Polynomial(p4)

        self.assertTrue(isinstance(p1, pl.Polynomial))
        self.assertTrue(isinstance(p2, pl.Polynomial))
        self.assertTrue(isinstance(p3, pl.Polynomial))
        self.assertTrue(isinstance(p4, pl.Polynomial))
        self.assertTrue(isinstance(p5, pl.Polynomial))

        self.assertEqual(p1.__str__(),"0")
        self.assertEqual(p2.__str__(),"8x3-5x2+3")
        self.assertEqual(p3.__str__(),"8x3-5x2+3")
        self.assertEqual(p4.__str__(),"-1x2+2x+5")
        self.assertEqual(p5.__str__(),"-1x2+2x+5")
	
    #@unittest.skip("demonstrating skipping")
    def test_Equal(self):
        print("test_Equal")
        p0 = pl.Polynomial()
        p1 = pl.Polynomial([])
        p2 = pl.Polynomial(0)
        self.assertTrue(p0 == p1)
        self.assertTrue(p1 == p2)
        self.assertTrue(p1 == [])
        self.assertTrue(() == p2)

        p1 = pl.Polynomial(1, 2, 4, 3)
        p2 = pl.Polynomial(1, 2, 4, 3)
        self.assertEqual(p1, p2)
        self.assertTrue(p1 == (1, 2, 4, 3))
        self.assertTrue((1, 2, 4, 3) == p2)

        p1 = pl.Polynomial(1, 2, 2, 1)
        p2 = pl.Polynomial([1, 2, 2, 1])
        p3 = pl.Polynomial((1, 2, 2, 1))
        self.assertTrue(p1 == p2)
        self.assertTrue(p2 == p3)
        self.assertTrue([1, 2, 2, 1] == p2)
        self.assertTrue([1, 2, 2, 1] == p2)
        self.assertFalse([1, 2, 2, 2] == p2)
        self.assertFalse(p2 == [1, 2, 2, 2])

        p4 = pl.Polynomial(0, 2, 2, 0)
        p5 = pl.Polynomial([0, 2, 2, 0])
        p6 = pl.Polynomial((0, 2, 2, 0))
        self.assertTrue(p4 == p5)
        self.assertTrue(p5 == p6)
        self.assertTrue((0, 2, 2, 0) == p4)
        self.assertTrue(p4 == [0, 2, 2, 0])
        self.assertFalse([1, 2, 2, 2] == p4)
        self.assertFalse(p4 == [1, 2, 2, 2])
        
    #@unittest.skip("demonstrating skipping")
    def test_NotEqualScalar(self):
        print("test_NotEqualScalar")
        #The test for scalar
        lastScalar = self.scalar_args_list[-1]
        lastScalar -= 110 # random number not equal 0
        lastPoly = pl.Polynomial(lastScalar)
        num_tests = len(self.scalar_args_list)
        for i in range(0,num_tests,1):
            agrs = self.scalar_args_list[i]
            poly = pl.Polynomial(agrs)
            poly_copy = pl.Polynomial(agrs)

            self.assertFalse(poly != poly_copy, "iteration = {0} of {1}".format(i, num_tests))
            self.assertFalse(poly != agrs, "iteration = {0} of {1}".format(i, num_tests))
            self.assertFalse(agrs != poly, "iteration = {0} of {1}".format(i, num_tests))

            self.assertTrue(poly != lastPoly, "iteration = {0} of {1}".format(i, num_tests))
            self.assertTrue(poly != lastScalar, "iteration = {0} of {1}".format(i, num_tests))

    #@unittest.skip("demonstrating skipping")
    def test_NotEqualList(self):
        print("test_NotEqualList")
        #The test for list
        lastList = self.seq1_args_list[-1][:]
        lastList[-2] -= 110 # random number not equal 0
        lastPoly = pl.Polynomial(lastList)
        num_tests = len(self.seq1_args_list)
        for i in range(0,num_tests,1):
            agrs = self.seq1_args_list[i]
            poly = pl.Polynomial(agrs)
            poly_copy = pl.Polynomial(agrs)

            self.assertFalse(poly != poly_copy, "iteration = {0} of {1}".format(i, num_tests))
            self.assertFalse(poly != agrs, "iteration = {0} of {1}".format(i, num_tests))
            self.assertFalse(agrs != poly, "iteration = {0} of {1}".format(i, num_tests))

            self.assertTrue(poly != lastPoly, "iteration = {0} of {1}".format(i, num_tests))
            self.assertTrue(poly != lastList, "iteration = {0} of {1}".format(i, num_tests))
    
    #@unittest.skip("demonstrating skipping")
    def test_NotEqualTuple(self):
        print("test_NotEqualTuple")
        #The test for tuple
        lastList = self.seq1_args_list[-1][:]
        lastList[-2] -= 110 # random number not equal 0
        lastPoly = pl.Polynomial(lastList)
        num_tests = len(self.seq2_args_list)
        for i in range(0,num_tests,1):
            agrs = self.seq2_args_list[i]
            poly = pl.Polynomial(agrs)
            poly_copy = pl.Polynomial(agrs)

            self.assertFalse(poly != poly_copy, "iteration = {0} of {1}".format(i, num_tests))
            self.assertFalse(poly != agrs, "iteration = {0} of {1}".format(i, num_tests))
            self.assertFalse(agrs != poly, "iteration = {0} of {1}".format(i, num_tests))

            self.assertTrue(poly != lastPoly, "iteration = {0} of {1}".format(i, num_tests))
            self.assertTrue(poly != tuple(lastList), "iteration = {0} of {1}".format(i, num_tests))
    
    #@unittest.skip("demonstrating skipping")
    def test_NotEqualEmpty(self):
        print("test_NotEqualEmpty")
        #The test for tuple
        lastList = self.seq1_args_list[-1][:]
        lastList[-2] -= 110 # random number not equal 0
        lastPoly = pl.Polynomial(lastList)
        
        #The test for empty
        self.assertTrue(lastPoly != [], "lastPoly != []")
        self.assertTrue([] != lastPoly, "[] != lastPoly")
        self.assertTrue(lastPoly != (), "lastPoly != ()")
        self.assertTrue(() != lastPoly, "() != lastPoly")
        self.assertFalse(pl.Polynomial([]) != [], "pl.Polynomial([]) != []")
         
    #@unittest.skip("demonstrating skipping")
    def test_EmptyPolynomial(self):
        print("test_EmptyPolynomial")
        test_list_args = ('', [], (), 0, (0,0), [0], [0,0,0], pl.Polynomial())

        for args in test_list_args:
            poly = pl.Polynomial(args)
            self.assertTrue(poly.IsEmpty())
            self.assertTrue(len(poly.coeffs)==0)
            self.assertEqual(poly, self.polyE)
            self.assertEqual(poly.__str__(),'0')

    #@unittest.skip("demonstrating skipping")
    def test_AddScalar(self):
        print("test_AddScalar")
        argsList_for_polys = self.seq1_args_list
        num_polys = len(argsList_for_polys)
        num_tests = len(self.scalar_args_list)
        for i in range(0, num_polys, 1):
            testPoly_args = argsList_for_polys[i]
            poly = pl.Polynomial(testPoly_args)
            for j in range(0, num_tests, 1):
                number = self.scalar_args_list[j]
                tmp_args = testPoly_args[:]
                tmp_args[-1] += number
                checkPoly = pl.Polynomial(tmp_args)
                save_poly = pl.Polynomial(poly)
                
                self.assertEqual(poly+number, checkPoly, "iteration = {0} of {1}".format(i*num_tests+j, num_tests*num_polys))
                self.assertEqual(number+poly, checkPoly, "iteration = {0} of {1}".format(i*num_tests+j, num_tests*num_polys))
                self.assertTrue(save_poly == poly, "The Polynomial must not mutable after these operations!!!")
                
    #@unittest.skip("demonstrating skipping")
    def test_AddSequenceOfScalar(self):
        print("test_AddSequenceOfScalar")
        sequenceOfScalar_list = self.seq1_args_list + self.seq2_args_list
        num_polynimials = len(sequenceOfScalar_list)
        for i in range(0, num_polynimials, 1):
            poly = pl.Polynomial(sequenceOfScalar_list[i])
            sequenceOfScalar = sequenceOfScalar_list[i][:]
            save_poly = pl.Polynomial(poly)
            
            self.assertEqual(poly+sequenceOfScalar, sequenceOfScalar+poly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(poly+sequenceOfScalar, poly*2, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(save_poly, poly, "The Polynomial must not mutable after these operations!!!")

    #@unittest.skip("demonstrating skipping")
    def test_AddPolynomial(self):
        print("test_AddPolynomial")
        args_list = self.empty_args_list + self.scalar_args_list + self.seq1_args_list + self.seq2_args_list
        num_polynimials = len(args_list)
        for i in range(0, num_polynimials, 1):
            poly = pl.Polynomial(args_list[i])
            same_poly = pl.Polynomial(args_list[i])
            save_poly1 = pl.Polynomial(poly)
            save_poly2 = pl.Polynomial(same_poly)
            
            self.assertEqual(poly+same_poly, same_poly+poly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(poly+same_poly, poly*2, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(save_poly1, poly, "The Polynomial must not mutable after these operations!!!")
            self.assertEqual(save_poly2, same_poly, "The Polynomial must not mutable after these operations!!!")
            

    #@unittest.skip("demonstrating skipping")
    def test_SubScalar(self):
        print("test_SubScalar")
        argsList_for_polys = self.seq1_args_list
        num_polys = len(argsList_for_polys)
        num_tests = len(self.scalar_args_list)
        
        for i in range(0, num_polys, 1):
            testPoly_args = argsList_for_polys[i]
            poly = pl.Polynomial(testPoly_args)
            for j in range(0, num_tests, 1):
                number = self.scalar_args_list[j]
                tmp_args = testPoly_args[:]
                tmp_args[-1] -= number
                check_right_Poly = pl.Polynomial(tmp_args)
                
                tmp_args = [-item for item in testPoly_args]
                tmp_args[-1] += number
                check_left_Poly = pl.Polynomial(tmp_args)
                save_poly = pl.Polynomial(poly)
                
                self.assertEqual(poly-number, check_right_Poly, "iteration = {0} of {1}".format(i*num_tests+j, num_tests*num_polys))
                self.assertEqual(number-poly, check_left_Poly, "iteration = {0} of {1}".format(i*num_tests+j, num_tests*num_polys))
                self.assertEqual(save_poly, poly, "The Polynomial must not mutable after these operations!!!")
            
    #@unittest.skip("demonstrating skipping")
    def test_SubSequenceOfScalar(self):
        print("test_SubSequenceOfScalar")
        sequenceOfScalar_list = self.seq1_args_list + self.seq2_args_list
        num_polynimials = len(sequenceOfScalar_list)
        for i in range(0, num_polynimials, 1):
            poly = pl.Polynomial(sequenceOfScalar_list[i])
            sequenceOfScalar = sequenceOfScalar_list[i][:]
            save_poly = pl.Polynomial(poly)
            
            self.assertEqual(-poly+sequenceOfScalar, sequenceOfScalar-poly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(poly, -(sequenceOfScalar-(poly*2)), "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(save_poly, poly, "The Polynomial must not mutable after these operations!!!")

    #@unittest.skip("demonstrating skipping")
    def test_SubPolynomial(self):
        print("test_SubPolynomial")
        args_list = self.empty_args_list + self.scalar_args_list + self.seq1_args_list + self.seq2_args_list
        num_polynimials = len(args_list)
        for i in range(0, num_polynimials, 1):
            poly = pl.Polynomial(args_list[i])
            same_poly = pl.Polynomial(args_list[i])
            save_poly1 = pl.Polynomial(poly)
            save_poly2 = pl.Polynomial(same_poly)
            
            self.assertEqual(-poly+same_poly, same_poly-poly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(poly,poly*2-same_poly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(save_poly1, poly, "The Polynomial must not mutable after these operations!!!")
            self.assertEqual(save_poly2, same_poly, "The Polynomial must not mutable after these operations!!!")


    #@unittest.skip("demonstrating skipping")
    def test_Negative(self):
        print("test_Negative")
        num_tests = len(self.seq1_args_list)
        for i in range(0,num_tests,1):
            poly = pl.Polynomial(self.seq1_args_list[i])  
            
            negation_args = [ -item for item in self.seq1_args_list[i] ]
            negation_poly = pl.Polynomial(negation_args)
            
            self.assertEqual(-poly, negation_poly, "iteration = {0} of {1}".format(i, num_tests))

    #@unittest.skip("demonstrating skipping")
    def test_ToString(self):
        print("test_ToString")
        num_tests = len(self.seq1_args_list)
        for i in range(0,num_tests,1):
            poly = pl.Polynomial(self.seq1_args_list[i])
            self.assertEqual(poly.__str__(), self.strPoly_list[i], "iteration = {0} of {1}".format(i, num_tests))
    
    #@unittest.skip("demonstrating skipping")
    def test_Negative_and_ToString(self):
        print("test_Negative_and_ToString")
        num_tests = len(self.seq1_args_list)
        for i in range(0,num_tests,1):
            poly = pl.Polynomial(self.seq1_args_list[i])
            self.assertEqual((-poly).__str__(), self.strNegPoly_list[i], "iteration = {0} of {1}".format(i, num_tests))
			
    #@unittest.skip("demonstrating skipping")
    def test_constructor_copy(self):
        print("test_constructor_copy")
        args_list = self.empty_args_list + self.scalar_args_list + self.seq1_args_list + self.seq2_args_list
        test_list_args = [pl.Polynomial(item) for item in args_list]
        
        for args in test_list_args:
            copy_poly = pl.Polynomial(args)
            self.assertEqual(copy_poly, args)
            self.assertTrue(copy_poly.__str__()==args.__str__())
            self.assertEqual(copy_poly.coeffs, args.coeffs)
    
    #@unittest.skip("demonstrating skipping")
    def test_constructor_multi_scalars(self):
        print("test_constructor_multi_scalars")
        test_list_args = [[1,2,3], [0,0,1,2,3], (1,2,3), (0,0,1,2,3), list([0,1,2,3])]
        
        polyExpect = pl.Polynomial(1,2,3)
        polyNotExpect = pl.Polynomial(3,2,1)
        for args in test_list_args:
            poly = pl.Polynomial(args)

            self.assertTrue(len(poly.coeffs)==3)
            self.assertEqual(poly, polyExpect)
            self.assertNotEqual(poly, polyNotExpect)
        
    #@unittest.skip("demonstrating skipping")
    def test_constructor_scalars(self):
        print(" test_constructor_scalars")

        test_list_args = [1, 1.75, 120000, 0.0000021, 120000.00031]
        test_list_args1 = [+item for item in test_list_args]
        test_list_args2 = [-item for item in test_list_args]

        for args in test_list_args:
            poly = pl.Polynomial(args)

            self.assertFalse(poly.IsEmpty())
            self.assertEqual(len(poly.coeffs),1)
            self.assertEqual(poly.__str__(),str(args))
            self.assertNotEqual(poly, self.polyE)

        for args in test_list_args1:
            poly = pl.Polynomial(args)

            self.assertFalse(poly.IsEmpty())
            self.assertEqual(len(poly.coeffs),1)
            self.assertEqual(poly.__str__(),str(args))
            self.assertNotEqual(poly, self.polyE)

        for args in test_list_args2:
            poly = pl.Polynomial(args)

            self.assertFalse(poly.IsEmpty())
            self.assertEqual(len(poly.coeffs), 1)
            self.assertEqual(poly.__str__(), str(args))
            self.assertNotEqual(poly, self.polyE)

     
    #@unittest.skip("demonstrating skipping")
    def test_MultScalar(self):
        print("test_MultScalar")
        argsList_for_polys = self.seq1_args_list
        num_polys = len(argsList_for_polys)
        num_tests = len(self.scalar_args_list)
        for i in range(0, num_polys, 1):
            testPoly_args = argsList_for_polys[i]
            poly = pl.Polynomial(testPoly_args)
            
            for j in range(0, num_tests, 1):
                number = self.scalar_args_list[j]
                tmp_args = testPoly_args[:]
                tmp_args = [item*number for item in tmp_args]
                checkPoly = pl.Polynomial(tmp_args)
                save_poly = pl.Polynomial(poly)
                
                self.assertEqual(poly*number, checkPoly, "iteration = {0} of {1}".format(i*num_tests+j, num_tests*num_polys))
                self.assertEqual(number*poly, checkPoly, "iteration = {0} of {1}".format(i*num_tests+j, num_tests*num_polys))
                self.assertEqual(save_poly, poly, "The Polynomial must not mutable after these operations!!!")
                
    #@unittest.skip("demonstrating skipping")
    def test_MultSequenceOfScalar(self):
        print("test_MultSequenceOfScalar")
        sequenceOfScalar_list = self.seq1_args_list
        num_polynimials = len(sequenceOfScalar_list)
        for i in range(0, num_polynimials, 1):
            polyA = pl.Polynomial(sequenceOfScalar_list[i])
            save_polyA = pl.Polynomial(polyA)

            sequenceOfScalar = self.testMultPoly[:]
            save_SOS = pl.Polynomial(sequenceOfScalar)

            answerPoly = pl.Polynomial(self.SolutionMultPoly[i])
            
            self.assertEqual(polyA*sequenceOfScalar, answerPoly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(sequenceOfScalar*polyA, answerPoly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(save_polyA, save_polyA, "The Polynomial must not mutable after these operations!!!")
            self.assertEqual(sequenceOfScalar, save_SOS, "The sequence must not mutable after these operations!!!")
            
            
    #@unittest.skip("demonstrating skipping")
    def test_MultPolynomial(self):
        print("test_MultPolynomial")
        args_list = self.seq1_args_list
        num_polynimials = len(args_list)
        for i in range(0, num_polynimials, 1):
            polyA = pl.Polynomial(args_list[i])
            save_polyA = pl.Polynomial(polyA)

            polyB = pl.Polynomial(self.testMultPoly)
            save_polyB = pl.Polynomial(polyB)

            answerPoly = pl.Polynomial(self.SolutionMultPoly[i])
            
            self.assertEqual(polyA*polyB, answerPoly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(polyB*polyA, answerPoly, "iteration = {0} of {1}".format(i, num_polynimials))
            self.assertEqual(save_polyA, save_polyA, "The Polynomial must not mutable after these operations!!!")
            self.assertEqual(save_polyB, save_polyB, "The Polynomial must not mutable after these operations!!!")
  

    #@unittest.skip("demonstrating skipping")
    def test_Exceptions_TypeError(self):
        print("test_Exceptions_TypeError")
        polyA = pl.Polynomial(self.seq1_args_list[0])
        save_polyA = pl.Polynomial(polyA)
        
        args_list_TE = self.exception_args_list_TypeError[:]
        
        num_polynimials = len(args_list_TE)
        for i in range(0, num_polynimials, 1):
            something = args_list_TE[i]
            with self.assertRaises(TypeError):
                polyA+something
            with self.assertRaises(TypeError):
                something+polyA
            with self.assertRaises(TypeError):
                polyA-something
            with self.assertRaises(TypeError):
                something-polyA
            with self.assertRaises(TypeError):
                polyA*something  
            with self.assertRaises(TypeError):
                something*polyA
            with self.assertRaises(TypeError):
                polyA == something
            with self.assertRaises(TypeError):
                polyA != something
            
            # polynomials must remain unchanged after tests!!!
            self.assertEqual(save_polyA, save_polyA, "The Polynomial must not mutable after these operations!!!")
            self.assertEqual(something, args_list_TE[i], "The sequence must not mutable after these operations!!!")

    #@unittest.skip("demonstrating skipping")
    def test_Exceptions_ValueError(self):
        print("test_Exceptions_ValueError")
        polyA = pl.Polynomial(self.seq1_args_list[0])
        save_polyA = pl.Polynomial(polyA)
        
        args_list_VE = self.exception_args_list_ValueError[:]
    
        num_polynimials = len(args_list_VE)
        for i in range(0, num_polynimials, 1):
            something = args_list_VE[i]
            with self.assertRaises(ValueError):
                polyA+something
            with self.assertRaises(ValueError):
                something+polyA
            with self.assertRaises(ValueError):
                polyA-something
            with self.assertRaises(ValueError):
                something-polyA
            with self.assertRaises(ValueError):
                polyA*something  
            with self.assertRaises(ValueError):
                something*polyA
            with self.assertRaises(ValueError):
                polyA == something
            with self.assertRaises(ValueError):
                polyA != something
            
            # polynomials must remain unchanged after tests!!!
            self.assertEqual(save_polyA, save_polyA, "The Polynomial must not mutable after these operations!!!")
            self.assertEqual(something, args_list_VE[i], "The sequence must not mutable after these operations!!!")
            

if __name__ == '__main__':
	unittest.main()
    
