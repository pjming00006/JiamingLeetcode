class PowerSum:
    def compute_power_sum(self, input_list, power=1):
        total = 0
        for item in input_list:
            if isinstance(item, list):
                sub_total = self.compute_power_sum(item, power+1)
                total += sub_total
            else:
                total += item
        total = total ** power
        print(total)
        return total

def main():
    solution = PowerSum()
    solution.compute_power_sum([2,3,[4,1,2]])
    solution.compute_power_sum([1,2,[3,4],[[2]]])

if __name__ == "__main__":
    main()