public class GeschenkeTausch {

    public static void main(String[] args) {
        int anzahlVerwandte = 3012210;
        int letzteStelle = iterativGeschenk(anzahlVerwandte);
        System.out.println("Bekommt alles: " + letzteStelle);
    }

    public static int iterativGeschenk(int anzahlVerwandte) {
        int[] verwandte = new int[anzahlVerwandte];
        for (int i = 0; i < anzahlVerwandte; i++) {
            verwandte[i] = 1; // Alle fangen mit einem Geschenk an
        }

        int mitspielendeVerwandte = anzahlVerwandte;
        int aktivePosition = 0; // Der 1. fängt an

        // Spielen bis nur genau ein Verwandter mitspielt
        while (mitspielendeVerwandte > 1) {
            int gegenueber = (aktivePosition + mitspielendeVerwandte / 2) % mitspielendeVerwandte;
            
            // Es werden alle Geschenke vom Gegenüber genommen
            verwandte[aktivePosition] += verwandte[gegenueber];
            verwandte[gegenueber] = 0;

            if (verwandte[gegenueber] == 0) { // Gegenüber ausgeschieden?
                mitspielendeVerwandte--;
            }

            aktivePosition = (gegenueber + 1) % mitspielendeVerwandte; // Durchlauf
        }

        for (int i = 0; i < anzahlVerwandte; i++) { // Suche
            if (verwandte[i] > 0) {
                return i + 1; // Array fängt bei 0 an -> 0 ist also 1. Person
            }
        }

        return -1; // Sicherheit
    }
}
