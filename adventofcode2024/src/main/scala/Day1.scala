object Day1 extends App with Day0 {

    private def part1(): Unit = {
        val input = readLines("day1.txt")
        for (line <- input) {
            println(line)
        }
    }

    private def part2(): Unit = {
        val input = readLine("day1.txt")
        println(input)
    }

    part1()
    part2()

}