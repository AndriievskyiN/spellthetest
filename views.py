from audioop import avg
import re
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import AllAnswer, CorrectAnswer, IncorrectAnswer, AllWords
from . import db
import json, os, random

easy_words =  ["word", "chess", "think", "easy", "computer", "water", "better", "letter","world", "thought"]
avg_words = ["throughout", "international", "internship", "entertainment", "confidence", "genre","sincere", "consultant", "weaknesses", "influence"]
hard_words = ["entrepreneurship", "psychologist","mnemonic","questionnaire","assassination","colleague","conscience","fluorescent","incidentally","reimbursement"]
all = []
views = Blueprint('views', __name__)

# random words 

def rnd_words_easy():
    random_word = random.choice(easy_words)
    global current_word_easy
    current_word_easy = AllWords(theword=random_word)
rnd_words_easy()

def rnd_words_avg():
    random_word = random.choice(avg_words)
    global current_word_avg
    current_word_avg = AllWords(theword=random_word)

rnd_words_avg()

def rnd_words_hard():
    random_word = random.choice(hard_words)
    global current_word_hard
    current_word_hard = AllWords(theword=random_word)
rnd_words_hard()

def rnd_words_all():
    for i in easy_words:
        for j in avg_words:
            for k in hard_words:
                all.append(i)
                all.append(j)
                all.append(k)
    random.shuffle(all)
    random_word = random.choice(all)
    global current_word_all
    current_word_all = AllWords(theword=random_word)
rnd_words_all()


# easy words

@views.route("/easy", methods=["GET", "POST"])
@login_required
def easy():
    if request.method == "POST":
        # listen button
        if "listen" in request.form:
            for i in range(1):
                os.system(f"say {current_word_easy.theword}")

        # submit button
        elif "submit" in request.form:
            answer =request.form.get("note")
            # correct answer
            if answer.lower() == current_word_easy.theword:
                cor_answer = CorrectAnswer(user_answer=answer,user_id = current_user.id)
                db.session.add(cor_answer)
                db.session.commit()
                rnd_words_easy()
                flash("Correct!")
                return redirect(url_for("views.easy"))

            
            # incorrect answer
            elif answer.lower() != current_word_easy.theword:
                inc_answer = IncorrectAnswer(word=current_word_easy.theword, user_answer = answer, user_id = current_user.id)
                db.session.add(inc_answer)
                db.session.commit()
                flash("Incorrect ;(", category="error")
        
            # adding all the answers
            all_answers = AllAnswer(user_id = current_user.id, word = current_word_easy.theword, user_answer=answer)
            db.session.add(all_answers)
            db.session.commit() 
    return render_template("easy.html", user = current_user)


# average words


@views.route("/average", methods=["GET", "POST"])
@login_required
def average():
    if request.method == "POST":

        # listen button
        if "listen" in request.form:
            for i in range(1):
                os.system(f"say {current_word_avg.theword}")

        # submit button
        elif "submit" in request.form:
            answer =request.form.get("note")
            # correct answer
            if answer.lower() == current_word_avg.theword:
                cor_answer = CorrectAnswer(user_answer=answer,user_id = current_user.id)
                db.session.add(cor_answer)
                db.session.commit()
                rnd_words_avg()
                flash("Correct!")
                return redirect(url_for("views.average"))

            
            # incorrect answer
            elif answer.lower() != current_word_avg.theword:
                inc_answer = IncorrectAnswer(word=current_word_avg.theword, user_answer = answer, user_id = current_user.id)
                db.session.add(inc_answer)
                db.session.commit()
                flash("Incorrect ;(", category="error")
        
            # adding all the answers
            all_answers = AllAnswer(user_id = current_user.id, word = current_word_avg.theword, user_answer=answer)
            db.session.add(all_answers)
            db.session.commit() 
    return render_template("average.html", user = current_user)   


# hard words


@views.route("/hard", methods=["GET", "POST"])
@login_required
def hard():
    if request.method == "POST":

        # listen button
        if "listen" in request.form:
            for i in range(1):
                os.system(f"say {current_word_hard.theword}")

        # submit button
        elif "submit" in request.form:
            answer =request.form.get("note")
            # correct answer
            if answer.lower() == current_word_hard.theword:
                cor_answer = CorrectAnswer(user_answer=answer,user_id = current_user.id)
                db.session.add(cor_answer)
                db.session.commit()
                rnd_words_hard()
                flash("Correct!")
                return redirect(url_for("views.hard"))

            
            # incorrect answer
            elif answer.lower() != current_word_hard.theword:
                inc_answer = IncorrectAnswer(word=current_word_hard.theword, user_answer = answer, user_id = current_user.id)
                db.session.add(inc_answer)
                db.session.commit()
                flash("Incorrect ;(", category="error")
        
            # adding all the answers
            all_answers = AllAnswer(user_id = current_user.id, word = current_word_hard.theword, user_answer=answer)
            db.session.add(all_answers)
            db.session.commit() 
    return render_template("hard.html", user = current_user)   


# words of all level


@views.route("/all", methods=["GET", "POST"])
@login_required
def all():
    if request.method == "POST":

        # listen button
        if "listen" in request.form:
            for i in range(1):
                os.system(f"say {current_word_all.theword}")

        # submit button
        elif "submit" in request.form:
            answer =request.form.get("note")
            # correct answer
            if answer.lower() == current_word_all.theword:
                cor_answer = CorrectAnswer(user_answer=answer,user_id = current_user.id)
                db.session.add(cor_answer)
                db.session.commit()
                rnd_words_all()
                flash("Correct!")
                return redirect(url_for("views.all"))

            
            # incorrect answer
            elif answer.lower() != current_word_all.theword:
                inc_answer = IncorrectAnswer(word=current_word_all.theword, user_answer = answer, user_id = current_user.id)
                db.session.add(inc_answer)
                db.session.commit()
                flash("Incorrect ;(", category="error")
        
            # adding all the answers
            all_answers = AllAnswer(user_id = current_user.id, word = current_word_all.theword, user_answer=answer)
            db.session.add(all_answers)
            db.session.commit() 
    return render_template("all.html", user = current_user)   




@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        if "easy" in request.form:
            return redirect(url_for('views.easy'))
    if request.method == "POST":
        if "average" in request.form:
            return redirect(url_for('views.average'))
    if request.method == "POST":
        if "hard" in request.form:
            return redirect(url_for('views.hard'))   
    if request.method == "POST":
        if "all" in request.form:
            return redirect(url_for('views.all'))       

    return render_template("home.html", user=current_user)
