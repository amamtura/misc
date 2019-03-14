import sys
import scrabble_challenge

cross_letters = [chr(x) for x in xrange(97, 123)]
cross_letters.insert(0, None) # the first word will not have a cross letter

def main():
    tile_pool = scrabble_challenge.TilePool()
    word_finder = scrabble_challenge.WordFinder()
    while len(tile_pool):
        letters = tile_pool.pop()
        for cross_letter in cross_letters:
            print '\nletters %s\ncross_letter %s\n\nresults below:' % (letters, cross_letter)
            for word, score in word_finder.list_words(letters, cross_letter):
                print word, score
        print '--- tile pool size now %s ---\n\n' % len(tile_pool)

if __name__=='__main__':
    main()
    sys.exit(0)

