import scala.io.Source

trait Day0 {

    def readLine(filename: String): String = {
      Source.fromResource(filename).getLines().next()
    }

    def readLines(filename: String): Iterator[String] = {
      Source.fromResource(filename).getLines().collect(s => s)
    }
}