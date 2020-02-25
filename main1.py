class Main:
    def partition(self,nums, low, high):
	    pivot = nums[high]
	    smaller = low-1
	    
	    for i in range(low,high):
	        if nums[i]<=pivot:
	            smaller+=1
	            
	            nums[smaller],nums[i] = nums[i], nums[smaller]
	    
	    nums[smaller+1], nums[high] = nums[high], nums[smaller+1]
	    return (smaller+1)
    
    def quick_sort(self,nums,low, high):
        if low<high:
            pi = self.partition(nums, low, high)
            self.quick_sort(nums, low, pi-1)
            self.quick_sort(nums, pi+1, high)
        return nums


    def readData(self):
        dir_path = r'C:\Users\m_manish\Desktop\LargeFile\\'
        file_path = 'file1.txt'
        with open(dir_path+file_path,'r') as f:
            l = []
            data = int(f.readline())
            l.append(data)
            curr_size = len(l)
            max_size = 50000000
            index = 1
            while data is not None:
                try:
                    data = int(f.readline())
                    if curr_size<=max_size:
                        l.append(data)
                        curr_size = len(l)
                    else:
                        l.sort()
                        with open(dir_path+"sort\\temp_"+str(index)+".txt",'w') as file:
                            #file.write(str(self.quick_sort(l,0,len(l)-1)))
                            file.write(str(l))
                            file.close()
                        index+=1
                        l=[]
                        l.append(data)
                        curr_size = len(l)
                except:
                    break
                
            l.sort()
            with open(dir_path+"sort\\temp_"+str(index)+".txt",'w') as file:
                file.write(str(l))
                #file.write(str(self.quick_sort(l,0,len(l)-1)))
                file.close()
        
        self.mergeChunks()
    

    def mergeChunks(self):
        pass            
                

if __name__=='__main__':
    m = Main()
    m.readData()
