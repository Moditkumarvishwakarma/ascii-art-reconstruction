
def generate_ascii():
    for row in range(1, 53):
        line = ""

        for column in range(80):
            char = " "  

            # ---------- ROW 1 ----------
            if row == 1:
                if 0 <= column <= 34:
                    char = "#"
                elif 35 <= column <= 37:
                    char = "%"
                elif 38 <= column <= 40:
                    char = "#"
                elif 41 <= column <= 45:
                    char = "%"
                elif 46 <= column <= 48:
                    char = "#"
                elif 49 <= column <= 79:
                    char = "*"

            # ---------- ROW 2 ----------
            elif row == 2:
                if 0 <= column <= 34:
                    char = "#"
                elif column == 35:
                    char = "%"
                elif 36 <= column <= 43:
                    char = "@"
                elif 44 <= column <= 48:
                    char = "%"
                elif 49 <= column <= 51:
                    char = "#"
                elif 52 <= column <= 56:
                    char = "*"
                elif 57 <= column <= 58:
                    char = "#"
                elif 59 <= column <= 79:
                    char = "*"

            # ---------- ROW 3 ----------
            elif row == 3:
                if 0 <= column <= 1:
                    char = "*"
                elif 2 <= column <= 23:
                    char = "#"
                elif column == 24:
                    char = "%"
                elif 25 <= column <= 26:
                    char = "#"
                elif column == 27:
                    char = "%"
                elif 28 <= column <= 30:
                    char = "#"
                elif column == 31:
                    char = "%"
                elif column == 32:
                    char = "#"
                elif 33 <= column <= 39:
                    char = "%"
                elif 40 <= column <= 46:
                    char = "@"
                elif 47 <= column <= 50:
                    char = "%"
                elif 51 <= column <= 54:
                    char = "#"
                elif 55 <= column <= 59:
                    char = "%"
                elif column == 60:
                    char = "#"
                elif 61 <= column <= 79:
                    char = "*"

            # ---------- ROW 4 ----------
            elif row == 4:
                if 0 <= column <= 5:
                    char = "*"
                elif 6 <= column <= 20:
                    char = "#"
                elif 21 <= column <= 33:
                    char = "%"
                elif 34 <= column <= 49:
                    char = "@"
                elif 50 <= column <= 54:
                    char = "%"
                elif column == 55:
                    char = "@"
                elif 56 <= column <= 61:
                    char = "%"
                elif column == 62:
                    char = "#"
                elif 63 <= column <= 79:
                    char = "*"

            # ---------- ROW 5 ----------
            elif row == 5:
                if 0 <= column <= 8:
                    char = "*"
                elif column == 9:
                    char = "#"
                elif 10 <= column <= 11:
                    char = "*"
                elif 12 <= column <= 18:
                    char = "#"
                elif 19 <= column <= 23:
                    char = "%"
                elif 24 <= column <= 31:
                    char = "@"
                elif column == 32:
                    char = "%"
                elif 33 <= column <= 62:
                    char = "@"
                elif column == 63:
                    char = "%"
                elif column == 64:
                    char = "#"
                elif 65 <= column <= 79:
                    char = "*"

            # ---------- ROW 6 ----------
            elif row == 6:
                if 0 <= column <= 14:
                    char = "*"
                elif 15 <= column <= 17:
                    char = "#"
                elif 18 <= column <= 19:
                    char = "%"
                elif 20 <= column <= 30:
                    char = "@"
                elif column == 31:
                    char = "%"
                elif 32 <= column <= 50:
                    char = "@"
                elif column == 51:
                    char = "%"
                elif 52 <= column <= 53:
                    char = "@"
                elif 54 <= column <= 55:
                    char = "%"
                elif 56 <= column <= 66:
                    char = "@"
                elif 67 <= column <= 79:
                    char = "*"

            # ---------- ROW 7 ----------
            elif row == 7:
                if 0 <= column <= 2:
                    char = "+"
                elif column == 3:
                    char = "*"
                elif column == 4:
                    char = "+"
                elif 5 <= column <= 13:
                    char = "*"
                elif column == 14:
                    char = "#"
                elif 15 <= column <= 20:
                    char = "%"
                elif 21 <= column <= 66:
                    char = "@"
                elif column == 67:
                    char = "%"
                elif 68 <= column <= 79:
                    char = "*"

            # ---------- ROW 8 ----------
            elif row == 8:
                if 0 <= column <= 5:
                    char = "+"
                elif 6 <= column <= 10:
                    char = "*"
                elif column == 11:
                    char = "#"
                elif 12 <= column <= 17:
                    char = "%"
                elif column == 18:
                    char = "@"
                elif column == 19:
                    char = "%"
                elif 20 <= column <= 66:
                    char = "@"
                elif 67 <= column <= 68:
                    char = "%"
                elif column == 69:
                    char = "#"
                elif 70 <= column <= 79:
                    char = "*"

            # ---------- ROW 9 ----------
            elif row == 9:
                if 0 <= column <= 8:
                    char = "+"
                elif column == 9:
                    char = "*"
                elif 10 <= column <= 17:
                    char = "%"
                elif column == 18:
                    char = "@"
                elif column == 19:
                    char = "%"
                elif 20 <= column <= 23:
                    char = "@"
                elif 24 <= column <= 25:
                    char = "%"
                elif 26 <= column <= 67:
                    char = "@"
                elif 68 <= column <= 70:
                    char = "%"
                elif 71 <= column <= 79:
                    char = "*"

            # ---------- ROW 10 ----------
            elif row == 10:
                if 0 <= column <= 8:
                    char = "+"
                elif column == 9:
                    char = "*"
                elif 10 <= column <= 11:
                    char = "%"
                elif column == 12:
                    char = "#"
                elif 13 <= column <= 16:
                    char = "%"
                elif column == 17:
                    char = "@"
                elif 18 <= column <= 20:
                    char = "%"
                elif column == 21:
                    char = "@"
                elif column == 22:
                    char = "%"
                elif column == 23:
                    char = "@"
                elif column == 24:
                    char = "%"
                elif 25 <= column <= 68:
                    char = "@"
                elif 69 <= column <= 70:
                    char = "%"
                elif column == 71:
                    char = "#"
                elif 72 <= column <= 79:
                    char = "*"

                        # ---------- ROW 11 ----------
            elif row == 11:
                if 0 <= column <= 9:
                    char = "+"
                elif 10 <= column <= 11:
                    char = "#"
                elif column == 12:
                    char = "%"
                elif 13 <= column <= 20:
                    char = "@"
                elif 21 <= column <= 23:
                    char = "%"
                elif 24 <= column <= 70:
                    char = "@"
                elif 71 <= column <= 72:
                    char = "%"
                elif 73 <= column <= 79:
                    char = "*"

            # ---------- ROW 12 ----------
            elif row == 12:
                if 0 <= column <= 7:
                    char = "+"
                elif column == 8:
                    char = "*"
                elif 9 <= column <= 12:
                    char = "%"
                elif 13 <= column <= 71:
                    char = "@"
                elif column == 72:
                    char = "%"
                elif 73 <= column <= 74:
                    char = "#"
                elif 75 <= column <= 79:
                    char = "*"

            # ---------- ROW 13 ----------
            elif row == 13:
                if 0 <= column <= 6:
                    char = "+"
                elif column == 7:
                    char = "*"
                elif column == 8:
                    char = "#"
                elif 9 <= column <= 10:
                    char = "%"
                elif column == 11:
                    char = "#"
                elif column == 12:
                    char = "%"
                elif 13 <= column <= 71:
                    char = "@"
                elif 72 <= column <= 74:
                    char = "%"
                elif column == 75:
                    char = "#"
                elif 76 <= column <= 79:
                    char = "*"

            # ---------- ROW 14 ----------
            elif row == 14:
                if 0 <= column <= 3:
                    char = "+"
                elif 4 <= column <= 6:
                    char = "*"
                elif column == 7:
                    char = "#"
                elif 8 <= column <= 11:
                    char = "%"
                elif 12 <= column <= 32:
                    char = "@"
                elif column == 33:
                    char = "%"
                elif 34 <= column <= 73:
                    char = "@"
                elif column == 74:
                    char = "%"
                elif 75 <= column <= 76:
                    char = "#"
                elif 77 <= column <= 79:
                    char = "*"

            # ---------- ROW 15 ----------
            elif row == 15:
                if 0 <= column <= 5:
                    char = "*"
                elif 6 <= column <= 7:
                    char = "#"
                elif 8 <= column <= 9:
                    char = "%"
                elif 10 <= column <= 74:
                    char = "@"
                elif 75 <= column <= 76:
                    char = "%"
                elif column == 77:
                    char = "#"
                elif 78 <= column <= 79:
                    char = "*"

            # ---------- ROW 16 ----------
            elif row == 16:
                if 0 <= column <= 1:
                    char = "*"
                elif 2 <= column <= 3:
                    char = "%"
                elif column == 4:
                    char = "#"
                elif 5 <= column <= 8:
                    char = "%"
                elif 9 <= column <= 40:
                    char = "@"
                elif 41 <= column <= 56:
                    char = "%"
                elif 57 <= column <= 76:
                    char = "@"
                elif column == 77:
                    char = "%"
                elif column == 78:
                    char = "#"
                elif column == 79:
                    char = "*"

            # ---------- ROW 17 ----------
            elif row == 17:
                if column == 0:
                    char = "*"
                elif column == 1:
                    char = "#"
                elif 2 <= column <= 7:
                    char = "%"
                elif 8 <= column <= 17:
                    char = "@"
                elif column == 18:
                    char = "%"
                elif 19 <= column <= 29:
                    char = "@"
                elif column == 30:
                    char = "%"
                elif 31 <= column <= 33:
                    char = "#"
                elif 34 <= column <= 37:
                    char = "%"
                elif 38 <= column <= 50:
                    char = "#"
                elif column == 51:
                    char = "%"
                elif 52 <= column <= 56:
                    char = "#"
                elif 57 <= column <= 58:
                    char = "%"
                elif 59 <= column <= 76:
                    char = "@"
                elif column == 77:
                    char = "%"
                elif column == 78:
                    char = "#"
                elif column == 79:
                    char = "*"

            # ---------- ROW 18 ----------
            elif row == 18:
                if 0 <= column <= 4:
                    char = "%"
                elif column == 5:
                    char = "@"
                elif 6 <= column <= 8:
                    char = "%"
                elif 9 <= column <= 26:
                    char = "@"
                elif 27 <= column <= 28:
                    char = "#"
                elif column == 29:
                    char = "%"
                elif column == 30:
                    char = "#"
                elif 31 <= column <= 32:
                    char = "*"
                elif 33 <= column <= 35:
                    char = "+"
                elif 36 <= column <= 40:
                    char = "*"
                elif 41 <= column <= 50:
                    char = "#"
                elif 51 <= column <= 57:
                    char = "*"
                elif 58 <= column <= 59:
                    char = "#"
                elif 60 <= column <= 61:
                    char = "%"
                elif 62 <= column <= 77:
                    char = "@"
                elif column == 78:
                    char = "%"
                elif column == 79:
                    char = "#"

            # ---------- ROW 19 ----------
            elif row == 19:
                if 0 <= column <= 2:
                    char = "%"
                elif 3 <= column <= 25:
                    char = "@"
                elif column == 26:
                    char = "%"
                elif 27 <= column <= 29:
                    char = "#"
                elif column == 30:
                    char = "+"
                elif 31 <= column <= 33:
                    char = "="
                elif column == 34:
                    char = "+"
                elif 35 <= column <= 37:
                    char = "="
                elif 38 <= column <= 40:
                    char = "+"
                elif 41 <= column <= 60:
                    char = "*"
                elif 61 <= column <= 62:
                    char = "#"
                elif 63 <= column <= 64:
                    char = "%"
                elif 65 <= column <= 77:
                    char = "@"
                elif 78 <= column <= 79:
                    char = "%"

            # ---------- ROW 20 ----------
            elif row == 20:
                if 0 <= column <= 24:
                    char = "@"
                elif column == 25:
                    char = "%"
                elif column == 26:
                    char = "*"
                elif column == 27:
                    char = "+"
                elif column == 28:
                    char = "*"
                elif column == 29:
                    char = "+"
                elif 30 <= column <= 38:
                    char = "="
                elif 39 <= column <= 44:
                    char = "+"
                elif column == 45:
                    char = "*"
                elif 46 <= column <= 47:
                    char = "#"
                elif 48 <= column <= 50:
                    char = "*"
                elif 51 <= column <= 64:
                    char = "#"
                elif column == 65:
                    char = "%"
                elif 66 <= column <= 78:
                    char = "@"
                elif column == 79:
                    char = "%"

                        # ---------- ROW 21 ----------
            elif row == 21:
                if 0 <= column <= 23:
                    char = "@"
                elif column == 24:
                    char = "%"
                elif column == 25:
                    char = "*"
                elif column == 26:
                    char = "+"
                elif column == 27:
                    char = "*"
                elif 28 <= column <= 29:
                    char = "+"
                elif 30 <= column <= 31:
                    char = "="
                elif 32 <= column <= 35:
                    char = "+"
                elif 36 <= column <= 40:
                    char = "*"
                elif 41 <= column <= 44:
                    char = "#"
                elif 45 <= column <= 46:
                    char = "%"
                elif column == 47:
                    char = "#"
                elif column == 48:
                    char = "+"
                elif column == 49:
                    char = "*"
                elif column == 50:
                    char = "#"
                elif 51 <= column <= 52:
                    char = "%"
                elif 53 <= column <= 64:
                    char = "@"
                elif 65 <= column <= 66:
                    char = "%"
                elif 67 <= column <= 79:
                    char = "@"

            # ---------- ROW 22 ----------
            elif row == 22:
                if column == 0:
                    char = "%"
                elif 1 <= column <= 22:
                    char = "@"
                elif column == 23:
                    char = "%"
                elif 24 <= column <= 25:
                    char = "#"
                elif column == 26:
                    char = "*"
                elif 27 <= column <= 28:
                    char = "+"
                elif column == 29:
                    char = "*"
                elif 30 <= column <= 31:
                    char = "#"
                elif 32 <= column <= 36:
                    char = "%"
                elif 37 <= column <= 38:
                    char = "@"
                elif column == 39:
                    char = "%"
                elif 40 <= column <= 45:
                    char = "@"
                elif column == 46:
                    char = "%"
                elif 47 <= column <= 49:
                    char = "#"
                elif 50 <= column <= 51:
                    char = "%"
                elif 52 <= column <= 66:
                    char = "@"
                elif column == 67:
                    char = "%"
                elif 68 <= column <= 79:
                    char = "@"

            # ---------- ROW 23 ----------
            elif row == 23:
                if column == 0:
                    char = "@"
                elif column == 1:
                    char = "%"
                elif 2 <= column <= 20:
                    char = "@"
                elif column == 21:
                    char = "%"
                elif column == 22:
                    char = "#"
                elif column == 23:
                    char = "*"
                elif 24 <= column <= 26:
                    char = "+"
                elif column == 27:
                    char = "*"
                elif column == 28:
                    char = "#"
                elif 29 <= column <= 45:
                    char = "%"
                elif column == 46:
                    char = "*"
                elif 47 <= column <= 48:
                    char = "+"
                elif column == 49:
                    char = "*"
                elif column == 50:
                    char = "#"
                elif 51 <= column <= 52:
                    char = "%"
                elif 53 <= column <= 57:
                    char = "@"
                elif 58 <= column <= 59:
                    char = "%"
                elif 60 <= column <= 61:
                    char = "#"
                elif 62 <= column <= 64:
                    char = "%"
                elif 65 <= column <= 66:
                    char = "@"
                elif column == 67:
                    char = "%"
                elif 68 <= column <= 79:
                    char = "@"

            # ---------- ROW 24 ----------
            elif row == 24:
                if column == 0:
                    char = "%"
                elif 1 <= column <= 19:
                    char = "@"
                elif column == 20:
                    char = "%"
                elif column == 21:
                    char = "#"
                elif column == 22:
                    char = "*"
                elif column == 23:
                    char = "+"
                elif 24 <= column <= 25:
                    char = "="
                elif column == 26:
                    char = "+"
                elif 27 <= column <= 30:
                    char = "*"
                elif 31 <= column <= 32:
                    char = "+"
                elif 33 <= column <= 34:
                    char = "*"
                elif column == 35:
                    char = "#"
                elif 36 <= column <= 42:
                    char = "%"
                elif column == 43:
                    char = "#"
                elif column == 44:
                    char = "*"
                elif column == 45:
                    char = "+"
                elif column == 46:
                    char = "="
                elif column == 47:
                    char = "-"
                elif 48 <= column <= 49:
                    char = "="
                elif column == 50:
                    char = "+"
                elif column == 51:
                    char = "#"
                elif 52 <= column <= 54:
                    char = "%"
                elif 55 <= column <= 62:
                    char = "@"
                elif column == 63:
                    char = "%"
                elif 64 <= column <= 65:
                    char = "#"
                elif column == 66:
                    char = "%"
                elif 67 <= column <= 68:
                    char = "#"
                elif 69 <= column <= 79:
                    char = "@"

            # ---------- ROW 25 ----------
            elif row == 25:
                if column == 0:
                    char = "%"
                elif 1 <= column <= 18:
                    char = "@"
                elif column == 19:
                    char = "%"
                elif column == 20:
                    char = "#"
                elif column == 21:
                    char = "+"
                elif 22 <= column <= 25:
                    char = "="
                elif column == 26:
                    char = "+"
                elif column == 27:
                    char = "*"
                elif 28 <= column <= 29:
                    char = "+"
                elif column == 30:
                    char = "*"
                elif column == 31:
                    char = "#"
                elif 32 <= column <= 35:
                    char = "%"
                elif 36 <= column <= 38:
                    char = "@"
                elif 39 <= column <= 41:
                    char = "%"
                elif column == 42:
                    char = "*"
                elif column == 43:
                    char = "+"
                elif 44 <= column <= 46:
                    char = "="
                elif 47 <= column <= 48:
                    char = "-"
                elif 49 <= column <= 50:
                    char = "="
                elif column == 51:
                    char = "*"
                elif 52 <= column <= 53:
                    char = "#"
                elif 54 <= column <= 58:
                    char = "%"
                elif 59 <= column <= 64:
                    char = "@"
                elif column == 65:
                    char = "%"
                elif 66 <= column <= 68:
                    char = "#"
                elif 69 <= column <= 79:
                    char = "@"

            # ---------- ROW 26 ----------
            elif row == 26:
                if 0 <= column <= 18:
                    char = "@"
                elif column == 19:
                    char = "%"
                elif column == 20:
                    char = "*"
                elif 21 <= column <= 24:
                    char = "="
                elif 25 <= column <= 27:
                    char = "+"
                elif column == 28:
                    char = "*"
                elif 29 <= column <= 31:
                    char = "#"
                elif 32 <= column <= 35:
                    char = "*"
                elif 36 <= column <= 40:
                    char = "#"
                elif column == 41:
                    char = "*"
                elif column == 42:
                    char = "+"
                elif 43 <= column <= 45:
                    char = "="
                elif 46 <= column <= 49:
                    char = "-"
                elif 50 <= column <= 51:
                    char = "="
                elif column == 52:
                    char = "*"
                elif 53 <= column <= 62:
                    char = "#"
                elif 63 <= column <= 64:
                    char = "*"
                elif 65 <= column <= 67:
                    char = "#"
                elif column == 68:
                    char = "*"
                elif column == 69:
                    char = "%"
                elif 70 <= column <= 79:
                    char = "@"

            # ---------- ROW 27 ----------
            elif row == 27:
                if 0 <= column <= 1:
                    char = "%"
                elif 2 <= column <= 17:
                    char = "@"
                elif column == 18:
                    char = "%"
                elif column == 19:
                    char = "#"
                elif column == 20:
                    char = "+"
                elif 21 <= column <= 23:
                    char = "="
                elif 24 <= column <= 28:
                    char = "-"
                elif 29 <= column <= 30:
                    char = ":"
                elif 31 <= column <= 32:
                    char = "-"
                elif column == 33:
                    char = "="
                elif 34 <= column <= 35:
                    char = "+"
                elif 36 <= column <= 37:
                    char = "*"
                elif 38 <= column <= 39:
                    char = "+"
                elif 40 <= column <= 41:
                    char = "="
                elif 42 <= column <= 50:
                    char = "-"
                elif column == 51:
                    char = "="
                elif column == 52:
                    char = "+"
                elif 53 <= column <= 62:
                    char = "*"
                elif 63 <= column <= 67:
                    char = "+"
                elif 68 <= column <= 69:
                    char = "*"
                elif 70 <= column <= 79:
                    char = "@"

            # ---------- ROW 28 ----------
            elif row == 28:
                if 0 <= column <= 16:
                    char = "@"
                elif 17 <= column <= 18:
                    char = "%"
                elif column == 19:
                    char = "*"
                elif 20 <= column <= 21:
                    char = "="
                elif 22 <= column <= 24:
                    char = "-"
                elif 25 <= column <= 26:
                    char = ":"
                elif 27 <= column <= 34:
                    char = "-"
                elif 35 <= column <= 39:
                    char = "="
                elif 40 <= column <= 50:
                    char = "-"
                elif 51 <= column <= 52:
                    char = "="
                elif 53 <= column <= 54:
                    char = "+"
                elif 55 <= column <= 61:
                    char = "*"
                elif 62 <= column <= 68:
                    char = "+"
                elif column == 69:
                    char = "*"
                elif column == 70:
                    char = "%"
                elif 71 <= column <= 79:
                    char = "@"

            # ---------- ROW 29 ----------
            elif row == 29:
                if 0 <= column <= 11:
                    char = "@"
                elif column == 12:
                    char = "%"
                elif 13 <= column <= 15:
                    char = "@"
                elif 16 <= column <= 17:
                    char = "%"
                elif column == 18:
                    char = "#"
                elif column == 19:
                    char = "+"
                elif 20 <= column <= 21:
                    char = "="
                elif 22 <= column <= 24:
                    char = "-"
                elif 25 <= column <= 28:
                    char = ":"
                elif 29 <= column <= 34:
                    char = "-"
                elif 35 <= column <= 36:
                    char = "="
                elif 37 <= column <= 38:
                    char = "-"
                elif column == 39:
                    char = "="
                elif 40 <= column <= 47:
                    char = "-"
                elif 48 <= column <= 49:
                    char = "="
                elif column == 50:
                    char = "+"
                elif 51 <= column <= 59:
                    char = "*"
                elif 60 <= column <= 68:
                    char = "+"
                elif column == 69:
                    char = "*"
                elif column == 70:
                    char = "#"
                elif column == 71:
                    char = "%"
                elif 72 <= column <= 78:
                    char = "@"
                elif column == 79:
                    char = "%"

            # ---------- ROW 30 ----------
            elif row == 30:
                if column == 0:
                    char = "%"
                elif 1 <= column <= 6:
                    char = "@"
                elif 7 <= column <= 9:
                    char = "%"
                elif 10 <= column <= 11:
                    char = "#"
                elif 12 <= column <= 13:
                    char = "%"
                elif column == 14:
                    char = "#"
                elif 15 <= column <= 17:
                    char = "%"
                elif column == 18:
                    char = "#"
                elif 19 <= column <= 22:
                    char = "="
                elif 23 <= column <= 27:
                    char = "-"
                elif 28 <= column <= 32:
                    char = ":"
                elif 33 <= column <= 38:
                    char = "-"
                elif 39 <= column <= 41:
                    char = "="
                elif 42 <= column <= 43:
                    char = "-"
                elif column == 44:
                    char = "+"
                elif column == 45:
                    char = "*"
                elif column == 46:
                    char = "#"
                elif column == 47:
                    char = "%"
                elif 48 <= column <= 52:
                    char = "#"
                elif 53 <= column <= 55:
                    char = "%"
                elif column == 56:
                    char = "#"
                elif 57 <= column <= 63:
                    char = "*"
                elif 64 <= column <= 66:
                    char = "+"
                elif 67 <= column <= 69:
                    char = "*"
                elif column == 70:
                    char = "#"
                elif 71 <= column <= 72:
                    char = "%"
                elif 73 <= column <= 76:
                    char = "@"
                elif column == 77:
                    char = "#"
                elif column == 78:
                    char = "*"
                elif column == 79:
                    char = "+"

                        # ---------- ROW 31 ----------
            elif row == 31:
                if column == 0: char = "%"
                elif 1 <= column <= 6: char = "@"
                elif column == 7: char = "#"
                elif column == 8: char = "%"
                elif column == 9: char = "*"
                elif 10 <= column <= 11: char = "+"
                elif 12 <= column <= 15: char = "#"
                elif 16 <= column <= 17: char = "*"
                elif column == 18: char = "+"
                elif 19 <= column <= 24: char = "="
                elif 25 <= column <= 38: char = "-"
                elif 39 <= column <= 43: char = "="
                elif column == 44: char = "*"
                elif column == 45: char = "#"
                elif column == 46: char = "*"
                elif 47 <= column <= 48: char = "+"
                elif column == 49: char = "*"
                elif column == 50: char = "#"
                elif column == 51: char = "%"
                elif 52 <= column <= 54: char = "#"
                elif column == 55: char = "%"
                elif column == 56: char = "#"
                elif 57 <= column <= 69: char = "*"
                elif 70 <= column <= 72: char = "#"
                elif 73 <= column <= 75: char = "@"
                elif column == 76: char = "%"
                elif column == 77: char = "*"
                elif column == 78: char = "="
                elif column == 79: char = "+"

            # ---------- ROW 32 ----------
            elif row == 32:
                if 0 <= column <= 1: char = "%"
                elif 2 <= column <= 6: char = "@"
                elif 7 <= column <= 8: char = "#"
                elif column == 9: char = "*"
                elif column == 10: char = "+"
                elif column == 11: char = "="
                elif column == 12: char = "*"
                elif column == 13: char = "#"
                elif column == 14: char = "%"
                elif column == 15: char = "#"
                elif column == 16: char = "+"
                elif 17 <= column <= 19: char = "="
                elif column == 20: char = "+"
                elif 21 <= column <= 29: char = "="
                elif 30 <= column <= 38: char = "-"
                elif column == 39: char = "="
                elif 40 <= column <= 44: char = "-"
                elif 45 <= column <= 48: char = "="
                elif 49 <= column <= 69: char = "*"
                elif column == 70: char = "#"
                elif column == 71: char = "%"
                elif column == 72: char = "#"
                elif 73 <= column <= 75: char = "%"
                elif column == 76: char = "#"
                elif column == 77: char = "="
                elif 78 <= column <= 79: char = "-"

            # ---------- ROW 33 ----------
            elif row == 33:
                if 0 <= column <= 1: char = "%"
                elif 2 <= column <= 6: char = "@"
                elif column == 7: char = "%"
                elif 8 <= column <= 9: char = "*"
                elif column == 10: char = "+"
                elif column == 11: char = "="
                elif column == 12: char = "*"
                elif 13 <= column <= 14: char = "#"
                elif column == 15: char = "*"
                elif 16 <= column <= 17: char = "-"
                elif 18 <= column <= 24: char = "="
                elif column == 25: char = "+"
                elif 26 <= column <= 30: char = "="
                elif 31 <= column <= 44: char = "-"
                elif 45 <= column <= 48: char = "="
                elif column == 49: char = "+"
                elif 50 <= column <= 51: char = "*"
                elif 52 <= column <= 53: char = "+"
                elif 54 <= column <= 57: char = "*"
                elif 58 <= column <= 59: char = "+"
                elif 60 <= column <= 68: char = "*"
                elif 69 <= column <= 72: char = "#"
                elif 73 <= column <= 74: char = "%"
                elif 75 <= column <= 77: char = "="
                elif 78 <= column <= 79: char = "-"

            # ---------- ROW 34 ----------
            elif row == 34:
                if column == 0: char = "#"
                elif 1 <= column <= 3: char = "%"
                elif 4 <= column <= 6: char = "@"
                elif 7 <= column <= 8: char = "%"
                elif column == 9: char = "+"
                elif column == 10: char = "*"
                elif column == 11: char = "="
                elif 12 <= column <= 13: char = "#"
                elif column == 14: char = "*"
                elif column == 15: char = "="
                elif column == 16: char = "+"
                elif 17 <= column <= 30: char = "="
                elif 31 <= column <= 42: char = "-"
                elif 43 <= column <= 45: char = "="
                elif 46 <= column <= 47: char = "-"
                elif column == 48: char = "="
                elif 49 <= column <= 52: char = "+"
                elif column == 53: char = "*"
                elif column == 54: char = "#"
                elif 55 <= column <= 56: char = "*"
                elif column == 57: char = "+"
                elif 58 <= column <= 71: char = "*"
                elif 72 <= column <= 74: char = "#"
                elif column == 75: char = "-"
                elif column == 76: char = ":"
                elif 77 <= column <= 79: char = "-"

            # ---------- ROW 35 ----------
            elif row == 35:
                if 0 <= column <= 3: char = "%"
                elif 4 <= column <= 6: char = "@"
                elif 7 <= column <= 9: char = "%"
                elif column == 10: char = "+"
                elif column == 11: char = "*"
                elif 12 <= column <= 13: char = "+"
                elif 14 <= column <= 30: char = "="
                elif 31 <= column <= 43: char = "-"
                elif column == 44: char = "+"
                elif 45 <= column <= 48: char = "*"
                elif 49 <= column <= 52: char = "#"
                elif column == 53: char = "%"
                elif 54 <= column <= 58: char = "#"
                elif 59 <= column <= 71: char = "*"
                elif column == 72: char = "+"
                elif 73 <= column <= 74: char = "%"
                elif 75 <= column <= 76: char = "+"
                elif column == 77: char = "*"
                elif column == 78: char = "+"
                elif column == 79: char = ":"

            # ---------- ROW 36 ----------
            elif row == 36:
                if 0 <= column <= 4: char = "%"
                elif 5 <= column <= 6: char = "@"
                elif 7 <= column <= 10: char = "%"
                elif column == 11: char = "+"
                elif 12 <= column <= 13: char = "="
                elif 14 <= column <= 15: char = "-"
                elif 16 <= column <= 17: char = "="
                elif column == 18: char = "-"
                elif 19 <= column <= 29: char = "="
                elif 30 <= column <= 37: char = "-"
                elif 38 <= column <= 39: char = "="
                elif 40 <= column <= 41: char = "+"
                elif column == 42: char = "*"
                elif 43 <= column <= 47: char = "#"
                elif column == 48: char = "*"
                elif 49 <= column <= 55: char = "#"
                elif 56 <= column <= 59: char = "%"
                elif 60 <= column <= 61: char = "#"
                elif 62 <= column <= 69: char = "*"
                elif column == 70: char = "+"
                elif column == 71: char = "*"
                elif column == 72: char = "#"
                elif 73 <= column <= 75: char = "%"
                elif column == 76: char = "#"
                elif column == 77: char = "="
                elif column == 78: char = "-"
                elif column == 79: char = ":"

            # ---------- ROW 37 ----------
            elif row == 37:
                if 0 <= column <= 2: char = "%"
                elif 3 <= column <= 8: char = "@"
                elif 9 <= column <= 11: char = "%"
                elif column == 12: char = "#"
                elif column == 13: char = "+"
                elif column == 14: char = "="
                elif 15 <= column <= 18: char = "+"
                elif 19 <= column <= 20: char = "*"
                elif column == 21: char = "+"
                elif 22 <= column <= 28: char = "="
                elif 29 <= column <= 36: char = "-"
                elif column == 37: char = "="
                elif 38 <= column <= 39: char = "+"
                elif 40 <= column <= 42: char = "*"
                elif 43 <= column <= 45: char = "="
                elif 46 <= column <= 47: char = "-"
                elif 48 <= column <= 50: char = "="
                elif 51 <= column <= 54: char = "+"
                elif 55 <= column <= 59: char = "*"
                elif 60 <= column <= 62: char = "#"
                elif 63 <= column <= 68: char = "*"
                elif column == 69: char = "#"
                elif column == 70: char = "*"
                elif column == 71: char = "#"
                elif 72 <= column <= 76: char = "%"
                elif column == 77: char = "*"
                elif column == 78: char = "+"
                elif column == 79: char = "*"

            # ---------- ROW 38 ----------
            elif row == 38:
                if 0 <= column <= 4: char = "%"
                elif 5 <= column <= 10: char = "@"
                elif 11 <= column <= 16: char = "%"
                elif 17 <= column <= 20: char = "#"
                elif column == 21: char = "*"
                elif column == 22: char = "+"
                elif 23 <= column <= 26: char = "="
                elif column == 27: char = "-"
                elif column == 28: char = "="
                elif 29 <= column <= 34: char = "-"
                elif 35 <= column <= 36: char = "="
                elif column == 37: char = "+"
                elif 38 <= column <= 39: char = "="
                elif 40 <= column <= 42: char = "-"
                elif 43 <= column <= 45: char = "="
                elif 46 <= column <= 47: char = "+"
                elif column == 48: char = "*"
                elif column == 49: char = "#"
                elif 50 <= column <= 53: char = "%"
                elif 54 <= column <= 58: char = "#"
                elif 59 <= column <= 62: char = "*"
                elif column == 63: char = "#"
                elif 64 <= column <= 68: char = "*"
                elif 69 <= column <= 70: char = "%"
                elif 71 <= column <= 72: char = "@"
                elif 73 <= column <= 77: char = "%"
                elif 78 <= column <= 79: char = "#"

            # ---------- ROW 39 ----------
            elif row == 39:
                if column == 0: char = "#"
                elif 1 <= column <= 2: char = "%"
                elif 3 <= column <= 9: char = "@"
                elif column == 10: char = "%"
                elif 11 <= column <= 13: char = "@"
                elif 14 <= column <= 18: char = "%"
                elif 19 <= column <= 20: char = "#"
                elif column == 21: char = "*"
                elif 22 <= column <= 23: char = "+"
                elif 24 <= column <= 28: char = "="
                elif 29 <= column <= 32: char = "-"
                elif 33 <= column <= 38: char = "="
                elif column == 39: char = "-"
                elif 40 <= column <= 41: char = "="
                elif 42 <= column <= 45: char = "+"
                elif column == 46: char = "*"
                elif 47 <= column <= 59: char = "#"
                elif 60 <= column <= 61: char = "*"
                elif 62 <= column <= 64: char = "#"
                elif 65 <= column <= 67: char = "*"
                elif column == 68: char = "#"
                elif 69 <= column <= 72: char = "@"
                elif 73 <= column <= 76: char = "%"
                elif column == 77: char = "#"
                elif column == 78: char = "="
                elif column == 79: char = "-"

            # ---------- ROW 40 ----------
            elif row == 40:
                if column == 0: char = "*"
                elif 1 <= column <= 3: char = "%"
                elif 4 <= column <= 16: char = "@"
                elif 17 <= column <= 18: char = "%"
                elif column == 19: char = "*"
                elif 20 <= column <= 25: char = "+"
                elif 26 <= column <= 50: char = "="
                elif 51 <= column <= 53: char = "+"
                elif 54 <= column <= 59: char = "*"
                elif column == 60: char = "#"
                elif 61 <= column <= 62: char = "*"
                elif 63 <= column <= 65: char = "#"
                elif column == 66: char = "*"
                elif column == 67: char = "#"
                elif column == 68: char = "%"
                elif 69 <= column <= 72: char = "@"
                elif 73 <= column <= 74: char = "%"
                elif column == 75: char = "#"
                elif column == 76: char = "="
                elif 77 <= column <= 78: char = "-"
                elif column == 79: char = ":"

                        # ---------- ROW 41 ----------
            elif row == 41:
                if column == 0: char = "*"
                elif column == 1: char = "#"
                elif 2 <= column <= 3: char = "%"
                elif 4 <= column <= 17: char = "@"
                elif column == 18: char = "%"
                elif column == 19: char = "#"
                elif 20 <= column <= 29: char = "+"
                elif 30 <= column <= 40: char = "="
                elif 41 <= column <= 48: char = "-"
                elif column == 49: char = "="
                elif 50 <= column <= 52: char = "+"
                elif 53 <= column <= 55: char = "*"
                elif 56 <= column <= 57: char = "+"
                elif 58 <= column <= 61: char = "*"
                elif 62 <= column <= 66: char = "#"
                elif column == 67: char = "%"
                elif 68 <= column <= 72: char = "@"
                elif 73 <= column <= 74: char = "%"
                elif column == 75: char = "#"
                elif column == 76: char = "+"
                elif column == 77: char = "="
                elif column == 78: char = "-"
                elif column == 79: char = ":"

            # ---------- ROW 42 ----------
            elif row == 42:
                if column == 0: char = "*"
                elif column == 1: char = "#"
                elif 2 <= column <= 4: char = "%"
                elif 5 <= column <= 17: char = "@"
                elif 18 <= column <= 19: char = "%"
                elif column == 20: char = "*"
                elif 21 <= column <= 31: char = "+"
                elif column == 32: char = "="
                elif column == 33: char = "+"
                elif 34 <= column <= 47: char = "="
                elif 48 <= column <= 49: char = "+"
                elif 50 <= column <= 53: char = "*"
                elif column == 54: char = "#"
                elif 55 <= column <= 57: char = "*"
                elif column == 58: char = "#"
                elif 59 <= column <= 60: char = "*"
                elif 61 <= column <= 65: char = "#"
                elif column == 66: char = "*"
                elif 67 <= column <= 71: char = "@"
                elif 72 <= column <= 74: char = "%"
                elif column == 75: char = "#"
                elif column == 76: char = "+"
                elif 77 <= column <= 78: char = "-"
                elif column == 79: char = ":"

            # ---------- ROW 43 ----------
            elif row == 43:
                if 0 <= column <= 1: char = "*"
                elif 2 <= column <= 4: char = "%"
                elif 5 <= column <= 17: char = "@"
                elif 18 <= column <= 19: char = "%"
                elif column == 20: char = "*"
                elif 21 <= column <= 43: char = "+"
                elif 44 <= column <= 48: char = "*"
                elif 49 <= column <= 64: char = "#"
                elif 65 <= column <= 66: char = "*"
                elif 67 <= column <= 71: char = "@"
                elif 72 <= column <= 74: char = "%"
                elif column == 75: char = "#"
                elif column == 76: char = "="
                elif 77 <= column <= 78: char = "-"
                elif column == 79: char = ":"

            # ---------- ROW 44 ----------
            elif row == 44:
                if column == 0: char = "+"
                elif column == 1: char = "*"
                elif column == 2: char = "#"
                elif 3 <= column <= 4: char = "%"
                elif 5 <= column <= 18: char = "@"
                elif column == 19: char = "%"
                elif column == 20: char = "*"
                elif 21 <= column <= 32: char = "+"
                elif 33 <= column <= 35: char = "*"
                elif column == 36: char = "+"
                elif column == 37: char = "*"
                elif column == 38: char = "+"
                elif 39 <= column <= 43: char = "*"
                elif 44 <= column <= 63: char = "#"
                elif column == 64: char = "*"
                elif column == 65: char = "#"
                elif column == 66: char = "*"
                elif column == 67: char = "%"
                elif 68 <= column <= 71: char = "@"
                elif 72 <= column <= 73: char = "%"
                elif column == 74: char = "#"
                elif column == 75: char = "*"
                elif 76 <= column <= 79: char = "-"

            # ---------- ROW 45 ----------
            elif row == 45:
                if 0 <= column <= 3: char = "*"
                elif column == 4: char = "#"
                elif column == 5: char = "%"
                elif 6 <= column <= 18: char = "@"
                elif column == 19: char = "%"
                elif column == 20: char = "*"
                elif 21 <= column <= 23: char = "+"
                elif 24 <= column <= 28: char = "="
                elif 29 <= column <= 34: char = "+"
                elif 35 <= column <= 41: char = "*"
                elif 42 <= column <= 63: char = "#"
                elif 64 <= column <= 66: char = "*"
                elif column == 67: char = "%"
                elif column == 68: char = "@"
                elif 69 <= column <= 73: char = "%"
                elif column == 74: char = "#"
                elif column == 75: char = "="
                elif 76 <= column <= 79: char = "-"

            # ---------- ROW 46 ----------
            elif row == 46:
                if 0 <= column <= 4: char = "*"
                elif 5 <= column <= 6: char = "#"
                elif column == 7: char = "%"
                elif 8 <= column <= 18: char = "@"
                elif column == 19: char = "%"
                elif column == 20: char = "#"
                elif 21 <= column <= 24: char = "+"
                elif 25 <= column <= 29: char = "="
                elif 30 <= column <= 34: char = "+"
                elif 35 <= column <= 41: char = "*"
                elif 42 <= column <= 48: char = "#"
                elif column == 49: char = "%"
                elif 50 <= column <= 63: char = "#"
                elif 64 <= column <= 66: char = "*"
                elif 67 <= column <= 69: char = "#"
                elif column == 70: char = "*"
                elif column == 71: char = "+"
                elif 72 <= column <= 79: char = "="

            # ---------- ROW 47 ----------
            elif row == 47:
                if 0 <= column <= 3: char = "*"
                elif 4 <= column <= 7: char = "#"
                elif column == 8: char = "%"
                elif 9 <= column <= 17: char = "@"
                elif 18 <= column <= 19: char = "%"
                elif column == 20: char = "#"
                elif 21 <= column <= 22: char = "+"
                elif 23 <= column <= 25: char = "="
                elif column == 26: char = "+"
                elif 27 <= column <= 30: char = "="
                elif 31 <= column <= 34: char = "+"
                elif 35 <= column <= 40: char = "*"
                elif 41 <= column <= 63: char = "#"
                elif 64 <= column <= 66: char = "*"
                elif 67 <= column <= 71: char = "+"
                elif 72 <= column <= 73: char = "="
                elif column == 74: char = "+"
                elif 75 <= column <= 79: char = "="

            # ---------- ROW 48 ----------
            elif row == 48:
                if 0 <= column <= 2: char = "*"
                elif 3 <= column <= 9: char = "#"
                elif column == 10: char = "%"
                elif 11 <= column <= 12: char = "@"
                elif 13 <= column <= 16: char = "%"
                elif 17 <= column <= 19: char = "#"
                elif column == 20: char = "*"
                elif column == 21: char = "+"
                elif 22 <= column <= 35: char = "="
                elif 36 <= column <= 37: char = "+"
                elif 38 <= column <= 40: char = "*"
                elif 41 <= column <= 49: char = "#"
                elif 50 <= column <= 51: char = "%"
                elif 52 <= column <= 62: char = "#"
                elif 63 <= column <= 66: char = "*"
                elif 67 <= column <= 79: char = "+"

            # ---------- ROW 49 ----------
            elif row == 49:
                if 0 <= column <= 2: char = "*"
                elif 3 <= column <= 10: char = "#"
                elif 11 <= column <= 13: char = "%"
                elif column == 14: char = "#"
                elif 15 <= column <= 16: char = "-"
                elif column == 17: char = "#"
                elif column == 18: char = "%"
                elif column == 19: char = "#"
                elif column == 20: char = "+"
                elif 21 <= column <= 38: char = "="
                elif 39 <= column <= 40: char = "+"
                elif 41 <= column <= 42: char = "*"
                elif 43 <= column <= 45: char = "#"
                elif 46 <= column <= 52: char = "%"
                elif 53 <= column <= 62: char = "#"
                elif 63 <= column <= 65: char = "*"
                elif column == 66: char = "+"
                elif column == 67: char = "="
                elif column == 68: char = "-"
                elif 69 <= column <= 79: char = "+"

            # ---------- ROW 50 ----------
            elif row == 50:
                if 0 <= column <= 2: char = "*"
                elif 3 <= column <= 12: char = "#"
                elif column == 13: char = "*"
                elif 14 <= column <= 15: char = "."
                elif column == 16: char = "="
                elif column == 17: char = "#"
                elif column == 18: char = "+"
                elif 19 <= column <= 38: char = "="
                elif 39 <= column <= 40: char = "+"
                elif 41 <= column <= 42: char = "*"
                elif 43 <= column <= 45: char = "#"
                elif 46 <= column <= 50: char = "%"
                elif 51 <= column <= 61: char = "#"
                elif 62 <= column <= 65: char = "*"
                elif 66 <= column <= 67: char = "+"
                elif 68 <= column <= 71: char = ":"
                elif 72 <= column <= 73: char = "-"
                elif 74 <= column <= 79: char = "+"

            # ---------- ROW 51 ----------
            elif row == 51:
                if 0 <= column <= 8: char = "*"
                elif column == 9: char = "="
                elif 10 <= column <= 11: char = ":"
                elif 12 <= column <= 15: char = "."
                elif column == 16: char = "-"
                elif column == 17: char = "+"
                elif 18 <= column <= 23: char = "="
                elif 24 <= column <= 28: char = "-"
                elif 29 <= column <= 37: char = "="
                elif 38 <= column <= 39: char = "+"
                elif 40 <= column <= 42: char = "*"
                elif 43 <= column <= 59: char = "#"
                elif 60 <= column <= 65: char = "*"
                elif 66 <= column <= 67: char = "+"
                elif 68 <= column <= 76: char = ":"
                elif column == 77: char = "="
                elif column == 78: char = "-"
                elif column == 79: char = "="

            # ---------- ROW 52 ----------
            elif row == 52:
                if 0 <= column <= 2: char = "*"
                elif column == 3: char = "+"
                elif column == 4: char = "-"
                elif column == 5: char = ":"
                elif 6 <= column <= 16: char = "."
                elif 17 <= column <= 18: char = "="
                elif 19 <= column <= 20: char = "-"
                elif 21 <= column <= 22: char = "="
                elif 23 <= column <= 31: char = "-"
                elif 32 <= column <= 37: char = "="
                elif 38 <= column <= 40: char = "+"
                elif 41 <= column <= 42: char = "*"
                elif 43 <= column <= 57: char = "#"
                elif 58 <= column <= 65: char = "*"
                elif column == 66: char = "+"
                elif column == 67: char = "-"
                elif 68 <= column <= 69: char = ":"
                elif column == 70: char = "."
                elif 71 <= column <= 73: char = ":"
                elif column == 74: char = "-"
                elif column == 75: char = ":"
                elif column == 76: char = "."
                elif 77 <= column <= 78: char = ":"
                elif column == 79: char = "-"

            line += char

        print(line)

 
generate_ascii()
