# -*- coding: utf-8 -*-
import unittest
import api

class QuoteTest(unittest.TestCase):

    def test_Reuben_Abel(self):
        quotes = api.get_all_quotes('Reuben_Abel')
        first_quote = quotes[0]
        wiki_quote = "The continuum in which we live is not the kind of place in which middles can be unambiguously excluded."
        self.assertEqual(wiki_quote, first_quote)

    def test_Hau_Pei_tsun_(self):
        correct_quotes = []
        correct_quotes.append("The slogans of \'countering back the mainland\' created by Chiang Kai-shek and \'liberating Taiwan\' by Mao Zedong several decades ago should be forgotten because none of them could be put into practice.")
        correct_quotes.append("When people on both sides of the Strait reach a consensus on their political system, unification will come to fruition naturally.")
        correct_quotes.append("Taiwanese independence is a dead end.")

        quotes = api.get_all_quotes('Hau Pei-tsun')
        self.assertEqual(set(quotes), set(correct_quotes))

    def test_Jack_Abbott(self):
        correct_quotes = []
        correct_quotes.append("Even European philosophers have taken notice that most of what we take for knowledge is nothing but bias and prejudice.")
        correct_quotes.append("The world is amazed at how 'cruel' it is! (This is very funny to think about!) And then, when the 'chips are down' (Sartre's favorite expression), Sartre, who has never gambled but is enamored of the terminology of a kind of daring that doesn't involve getting his ass skinned, 'martyrs' himself. It is the same kind of responsibility anyone takes upon himself by submitting to your bad opinion of him by hanging his head and agreeing with all the accusations - and then, when he has done that, forlornly tells you he is sorry it rained last night, sorry the price of tea went up, etc. etc.")
        correct_quotes.append("Most important, you learn never to trust a man, even if he seems honest and sincere. You learn how men deceive themselves and how impossible it is to help them without injuring yourself.")
        correct_quotes.append("The mind does not regulate its own condition. Mental depression, for example, is a state of mind caused by the body. In a cell in the hole it only seems that there is a separation of mind and body - in fact, the body's condition (of deprivation of sensations; experiences, functions, and so on) controls the moods of the mind more than in any other situation I can think of.")
        correct_quotes.append("The intelligence recedes, no more a tool of learning - because knowledge is based on experience - but a tool of the outside world it is deprived of knowing. It tries to contact other minds by telepathy; it becomes the Ancestor. Words and Numbers come to hold mystic significance: they were invented by some arcane magic older than man. The line between the word and the thing vanishes; the intervals of numbers in infinity collapse with infinity.")
        correct_quotes.append("But a kind of genius can come of this deprivation of sensation, of experience. It has been mistaken as naїve intelligence, when in fact it is empty intelligence, pure intelligence. The composition of the mind is altered. Its previous cultivation is disintegrated and it has greater access to the brain, the body: it is Supersanity. Learning is turned inside out. You have to start from the top and work your way down. You must study mathematical theory before simple arithmetic; theoretical physics before applied physics; anatomy, you might say, before you can walk.")
        correct_quotes.append("I feel that if I ever did adjust to prison, I could by that alone never adjust to society.")
        correct_quotes.append("This world is nothing. An illusion. Death is the release.")

        quotes = api.get_all_quotes('Jack_Abbott')

        self.assertEqual(set(quotes), set(correct_quotes))


    def test_Dijkstra(self):
        correct_quotes = []

        correct_quotes.append("For a number of years I have been familiar with the observation that the quality of programmers is a decreasing function of the density of go to statements in the programs they produce. More recently I discovered why the use of the go to statement has such disastrous effects, and I became convinced that the go to statement should be abolished from all \"higher level\" programming languages.")
        correct_quotes.append("A convincing demonstration of correctness being impossible as long as the mechanism is regarded as a black box, our only hope lies in not regarding the mechanism as a black box.")
        correct_quotes.append("As a result of a long sequence of coincidences I entered the programming profession officially on the first spring morning of 1952, and as far as I have been able to trace, I was the first Dutchman to do so in my country.")
        correct_quotes.append("The use of COBOL cripples the mind; its teaching should, therefore, be regarded as a criminal offense.")
        correct_quotes.append("Thank goodness we don't have only serious problems, but ridiculous ones as well.")
        correct_quotes.append("When I came back from Munich, it was September, and I was Professor of Mathematics at the Eindhoven University of Technology. Later I learned that I had been the Department's third choice, after two numerical analysts had turned the invitation down; the decision to invite me had not been an easy one, on the one hand because I had not really studied mathematics, and on the other hand because of my sandals, my beard and my \"arrogance\" (whatever that may be).")
        correct_quotes.append("The required techniques of effective reasoning are pretty formal, but as long as programming is done by people that don't master them, the software crisis will remain with us and will be considered an incurable disease. And you know what incurable diseases do: they invite the quacks and charlatans in, who in this case take the form of Software Engineering gurus.")
        correct_quotes.append("In short, I suggest that the programmer should continue to understand what he is doing, that his growing product remains firmly within his intellectual grip. It is my sad experience that this suggestion is repulsive to the average experienced programmer, who clearly derives a major part of his professional excitement from not quite understanding what he is doing. In this streamlined age, one of our most undernourished psychological needs is the craving for Black Magic and apparently the automatic computer can satisfy this need for the professional software engineer, who is secretly enthralled by the gigantic risks he takes in his daring irresponsibility. For his frustrations I have no remedy......")
        correct_quotes.append("The precious gift that this Turing Award acknowledges is Dijkstra's style: his approach to programming as a high, intellectual challenge; his eloquent insistence and practical demonstration that programs should be composed correct, not just debugged into correctness; and his illuminating perception of problems at the foundations of program design.")

        incorrect_quotes = []
        incorrect_quotes.append("Computer Science is no more about computers than astronomy is about telescopes.")
        incorrect_quotes.append("Go To statement considered harmful")

        quotes = api.get_all_quotes('Edsger_W._Dijkstra')

        self.assertTrue(set(correct_quotes).issubset(set(quotes)))
        self.assertFalse(set(incorrect_quotes).issubset(set(quotes)))

    #
    # def test_Aristotles(self):


def main():
    unittest.main()

if __name__ == '__main__':
    main()
