#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## secondhamza verbs
## ----------------------------------------------------------------------------##


def secondhamza_past_actv(base, base_t, base_n, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.past.p3.m.sg'] = [(base, '-', '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-')];
		forms['actv.past.p2.m.sg'] = [(base_t + 'ت', '-', '-')];
		forms['actv.past.p2.f.sg'] = [(base_t + 'ت', '-', '-')];
		forms['actv.past.p1.mf.sg'] = [(base_t + 'ت', '-', '-')];

		forms['actv.past.p3.m.du'] = [(base + 'ا', '-', '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-')];
		forms['actv.past.p2.mf.du'] = [(base_t + 'تما', '-', '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.pl'] = [(base_n + 'ن', '-', '-')];
		forms['actv.past.p2.m.pl'] = [(base_t + 'تم', '-', '-')];
		forms['actv.past.p2.f.pl'] = [(base_t + 'تن', '-', '-')];
		forms['actv.past.p1.mf.pl'] = [(base_n + 'نا', '-', '-')];
	#}
	else : #{
		forms['actv.past.p3.m.sg'] = [(base, '-', '-'), (base, paradigm, '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-'), (base + 'ت', paradigm, '-')];
		forms['actv.past.p2.m.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', paradigm, '-')];
		forms['actv.past.p2.f.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', paradigm, '-')];
		forms['actv.past.p1.mf.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', paradigm, '-')];

		forms['actv.past.p3.m.du'] = [(base + 'ا', '-', '-'), (base + 'ا', paradigm, '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-'), (base + 'تا', paradigm, '-')];
		forms['actv.past.p2.mf.du'] = [(base_t + 'تما', '-', '-'), (base_t + 'تما', paradigm, '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.past.p3.f.pl'] = [(base_n + 'ن', '-', '-'), (base_n + 'ن', paradigm, '-')];
		forms['actv.past.p2.m.pl'] = [(base_t + 'تم', '-', '-'), (base_t + 'تمو', paradigm, '-')];
		forms['actv.past.p2.f.pl'] = [(base_t + 'تن', '-', '-'), (base_t + 'تن', paradigm, '-')];
		forms['actv.past.p1.mf.pl'] = [(base_n + 'نا', '-', '-'), (base_n + 'نا', paradigm, '-')];
	#}

	return forms;
#}


def secondhamza_past_pasv(base, base_t, base_n): #{

	forms = {};

	rlbase = base[0: 2] + 'ُ' + base[2: ];
	rlbase_t = base_t[0: 2] + 'ُ' + base_t[2: ];
	rlbase_n = base_n[0: 2] + 'ُ' + base_n[2: ];	


	forms['pasv.past.p3.m.sg'] = [(base, '-', 'LR'), (rlbase, '-', 'RL')];
	forms['pasv.past.p3.f.sg'] = [(base + 'ت', '-', 'LR'), (rlbase + 'ت', '-', 'RL')];
	forms['pasv.past.p2.m.sg'] = [(base_t + 'ت', '-', 'LR'), (rlbase_t + 'ت', '-', 'RL')];
	forms['pasv.past.p2.f.sg'] = [(base_t + 'ت', '-', 'LR'), (rlbase_t + 'ت', '-', 'RL')];
	forms['pasv.past.p1.mf.sg'] = [(base_t + 'ت', '-', 'LR'), (rlbase_t + 'ت', '-', 'RL')];

	forms['pasv.past.p3.m.du'] = [(base + 'ا', '-', 'LR'), (rlbase + 'ا', '-', 'RL')];
	forms['pasv.past.p3.f.du'] = [(base + 'تا', '-', 'LR'), (rlbase + 'تا', '-', 'RL')];
	forms['pasv.past.p2.mf.du'] = [(base_t + 'تما', '-', 'LR'), (rlbase_t + 'تما', '-', 'RL')];

	forms['pasv.past.p3.m.pl'] = [(base + 'وا', '-', 'LR'), (rlbase + 'وا', '-', 'RL')];
	forms['pasv.past.p3.f.pl'] = [(base_n + 'ن', '-', 'LR'), (rlbase_n + 'ن', '-', 'RL')];
	forms['pasv.past.p2.m.pl'] = [(base_t + 'تم', '-', 'LR'), (rlbase_t + 'تم', '-', 'RL')];
	forms['pasv.past.p2.f.pl'] = [(base_t + 'تن', '-', 'LR'), (rlbase_t + 'تن', '-', 'RL')];
	forms['pasv.past.p1.mf.pl'] = [(base_n + 'نا', '-', 'LR'), (rlbase_n + 'نا', '-', 'RL')];

	return forms;
#}


def secondhamza_pres_actv(base, base_n, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
	
		forms['actv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', paradigm, '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', paradigm, '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm, '-')];

	#}

	return forms;
#}



def secondhamza_pres_pasv(base, base_n): #{

	forms = {};

	forms['pasv.pres.p3.m.sg'] = [('ي' + base, '-', 'LR'), ('يُ' + base, '-', 'RL')];
	forms['pasv.pres.p3.f.sg'] = [('ت' + base, '-', 'LR'), ('تُ' + base, '-', 'RL')];
	forms['pasv.pres.p2.m.sg'] = [('ت' + base, '-', 'LR'), ('تُ' + base, '-', 'RL')];
	forms['pasv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', 'LR'), ('تُ' + base + 'ين', '-', 'RL')];
	forms['pasv.pres.p1.mf.sg'] = [('أ' + base, '-', 'LR'), ('اُ' + base, '-', 'RL')];

	forms['pasv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', 'LR'), ('يُ' + base + 'ان', '-', 'RL')];
	forms['pasv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', 'LR'), ('تُ' + base + 'ان', '-', 'RL')];
	forms['pasv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', 'LR'), ('تُ' + base + 'ان', '-', 'RL')];

	forms['pasv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', 'LR'), ('يُ' + base + 'ون', '-', 'RL')];
	forms['pasv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', 'LR'), ('يُ' + base_n + 'ن', '-', 'RL')];
	forms['pasv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', 'LR'), ('تُ' + base + 'ون', '-', 'RL')];
	forms['pasv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', 'LR'), ('تُ' + base_n + 'ن', '-', 'RL')];
	forms['pasv.pres.p1.mf.pl'] = [('ن' + base, '-', 'LR'), ('نُ' + base, '-', 'RL')];

	return forms;
#}



def secondhamza_subjun_actv(base, base_n, subtype, tv): #{

	forms = {};

	paradigm = 'S__فتح/ه';
	paradigm_cons = 'S__فتح/ه';

	if subtype == 'n' :
		paradigm_cons = 'S__يلون/ه';
	elif subtype == 'k' :
		paradigm_cons = 'S__يترك/ه';
	elif subtype == 'h' :
		paradigm_cons = 'S__يشبه/ه';

	if tv == 'iv' : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm_cons, '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm_cons, '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm_cons, '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm_cons, '-')];
	
		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', paradigm, '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', paradigm, '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm_cons, '-')];
	#}

	return forms;
#}


def secondhamza_subjun_pasv(base, base_n): #{

	forms = {};

	forms['pasv.subjun.p3.m.sg'] = [('ي' + base, '-', 'LR'), ('يُ' + base, '-', 'RL')];
	forms['pasv.subjun.p3.f.sg'] = [('ت' + base, '-', 'LR'), ('تُ' + base, '-', 'RL')];
	forms['pasv.subjun.p2.m.sg'] = [('ت' + base, '-', 'LR'), ('تُ' + base, '-', 'RL')];
	forms['pasv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', 'LR'), ('تُ' + base + 'ي', '-', 'RL')];
	forms['pasv.subjun.p1.mf.sg'] = [('أ' + base, '-', 'LR'), ('اُ' + base, '-', 'RL')];

	forms['pasv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', 'LR'), ('يُ' + base + 'ا', '-', 'RL')];
	forms['pasv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', 'LR'), ('تُ' + base + 'ا', '-', 'RL')];
	forms['pasv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', 'LR'), ('تُ' + base + 'ا', '-', 'RL')];

	forms['pasv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', 'LR'), ('يُ' + base + 'وا', '-', 'RL')];
	forms['pasv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', 'LR'), ('يُ' + base_n + 'ن', '-', 'RL')];
	forms['pasv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', 'LR'), ('تُ' + base + 'وا', '-', 'RL')];
	forms['pasv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', 'LR'), ('تُ' + base_n + 'ن', '-', 'RL')];
	forms['pasv.subjun.p1.mf.pl'] = [('ن' + base, '-', 'LR'), ('نُ' + base, '-', 'RL')];

	return forms;
#}


def secondhamza_apocop_actv(base, base_n, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
	
		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', paradigm, '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', paradigm, '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm, '-')];
	#}

	return forms;
#}


def secondhamza_apocop_pasv(base, base_n): #{

	forms = {};

	forms['pasv.apocop.p3.m.sg'] = [('ي' + base, '-', 'LR'), ('يُ' + base, '-', 'RL')];
	forms['pasv.apocop.p3.f.sg'] = [('ت' + base, '-', 'LR'), ('تُ' + base, '-', 'RL')];
	forms['pasv.apocop.p2.m.sg'] = [('ت' + base, '-', 'LR'), ('تُ' + base, '-', 'RL')];
	forms['pasv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', 'LR'), ('تُ' + base + 'ي', '-', 'RL')];
	forms['pasv.apocop.p1.mf.sg'] = [('أ' + base, '-', 'LR'), ('اُ' + base, '-', 'RL')];

	forms['pasv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', 'LR'), ('يُ' + base + 'ا', '-', 'RL')];
	forms['pasv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', 'LR'), ('تُ' + base + 'ا', '-', 'RL')];
	forms['pasv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', 'LR'), ('تُ' + base + 'ا', '-', 'RL')];

	forms['pasv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', 'LR'), ('يُ' + base + 'وا', '-', 'RL')];
	forms['pasv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', 'LR'), ('يُ' + base_n + 'ن', '-', 'RL')];
	forms['pasv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', 'LR'), ('تُ' + base + 'وا', '-', 'RL')];
	forms['pasv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', 'LR'), ('تُ' + base_n + 'ن', '-', 'RL')];
	forms['pasv.apocop.p1.mf.pl'] = [('ن' + base, '-', 'LR'), ('نُ' + base, '-', 'RL')];

	return forms;
#}


def secondhamza_imp(base, base_n, subtype, tv): #{

	# passive voice?

	forms = {};

	paradigm = 'S__فتح/ه';
	paradigm_cons = 'S__فتح/ه';

	if subtype == 'n' :
		paradigm_cons = 'S__يلون/ه';
	elif subtype == 'k' :
		paradigm_cons = 'S__يترك/ه';
	elif subtype == 'h' :
		paradigm_cons = 'S__يشبه/ه';


	if tv == 'iv' : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', '-')];
	#}
	else : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-'), (base, paradigm_cons, '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-'), (base + 'ي', paradigm, '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', '-'), (base + 'ا', paradigm, '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', '-'), (base_n + 'ن', paradigm, '-')];
	#}

	return forms ; 
#}


def secondhamza_pprs(base, r): #{

        forms = {};

	forms['pprs.m.sg'] = [(base, 'S__بيت/', r)] ;
	forms['pprs.f.sg'] = [(base, 'S__كلم/ة', r)] ;
	forms['pprs.m.pl'] = [(base, 'S__مهندس/ون', r)] ;
	forms['pprs.f.pl'] = [(base + 'ات', 'S__كلمات/', r)] ;

	return forms;
#}


def secondhamza_pp(base, r): #{

        forms = {};

	forms['pp.m.sg'] = [(base, 'S__بيت/', r)] ;
	forms['pp.f.sg'] = [(base, 'S__كلم/ة', r)] ;
	forms['pp.m.pl'] = [(base, 'S__مهندس/ون', r)] ;
	forms['pp.f.pl'] = [(base + 'ات', 'S__كلمات/', r)] ;

	return forms;
#}




## ----------------------------------------------------------------------------##
## pattern 1
## ----------------------------------------------------------------------------##


def secondhamza_patt1_past(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if v[1] == 'a' :
		r1 = 'أ';
	elif v[1] == 'i' :
		r1 = 'ئ';
	else : # v[1] == 'u'
		r1 = 'ؤ';

	base = r[0] + r1 + r[2];

	if r[2] == 'ت' :
		base_t = r[0] + r1;
	else :
		base_t = r[0] + r1 + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r1;
	else :
		base_n = r[0] + r1 + r[2];

	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		r1 = 'ئ';

		base = r[0] + r1 + r[2];

		if r[2] == 'ت' :
			base_t = r[0] + r1;
		else :
			base_t = r[0] + r1 + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + r1;
		else :
			base_n = r[0] + r1 + r[2];

		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}



def secondhamza_patt1_pres(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if v[1] == 'a' :
		r1 = 'أ';
	elif v[1] == 'i' :
		r1 = 'ئ';
	else : # v[1] == 'u'
		r1 = 'ؤ';

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	base = r[0] + r1 + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r1;
	else :
		base_n = r[0] + r1 + r[2];

	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));

	base = 'ا' + base;
	base_n = 'ا' + base_n;

	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{
		r1 = 'أ';

		base = r[0] + r1 + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + r1;
		else :
			base_n = r[0] + r1 + r[2];

		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}



def secondhamza_patt1_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs(r[0] + 'ائ' + r[2], '-');
#}


def secondhamza_patt1_pp(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pp('م' + r[0] + 'ؤو' + r[2], '-');
#}


## ----------------------------------------------------------------------------##
## pattern 2
## ----------------------------------------------------------------------------##


def secondhamza_patt2_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'أ' + r[2];

	if r[2] == 'ت' :
		base_t = r[0] + 'أ';
	else :
		base_t = r[0] + 'أ' + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'أ';
	else :
		base_n = r[0] + 'أ' + r[2];

	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = r[0] + 'ئ' + r[2];

		if r[2] == 'ت' :
			base_t = r[0] + 'ئ';
		else :
			base_t = r[0] + 'ئ' + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + 'ئ';
		else :
			base_n = r[0] + 'ئ' + r[2];

		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def secondhamza_patt2_pres(root, tv): #{
	r = root.split('-'); # radicals

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	base = r[0] + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ئ';
	else :
		base_n = r[0] + 'ئ' + r[2];

	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));
	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{

		base = r[0] + 'أ' + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + 'أ';
		else :
			base_n = r[0] + 'أ' + r[2];

		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}



def secondhamza_patt2_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs('م' + r[0] + 'ئ' + r[2], '-');
#}


def secondhamza_patt2_pp(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pp('م' + r[0] + 'أ' + r[2], '-');
#}


## ----------------------------------------------------------------------------##
## pattern 3
## ----------------------------------------------------------------------------##


def secondhamza_patt3_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'اء' + r[2];

	if r[2] == 'ت' :
		base_t = r[0] + 'اء';
	else :
		base_t = r[0] + 'اء' + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'اء';
	else :
		base_n = r[0] + 'اء' + r[2];

	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = r[0] + 'وئ' + r[2];

		if r[2] == 'ت' :
			base_t = r[0] + 'وئ';
		else :
			base_t = r[0] + 'وئ' + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + 'وئ';
		else :
			base_n = r[0] + 'وئ' + r[2];

		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def secondhamza_patt3_pres(root, tv): #{
	r = root.split('-'); # radicals

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';


	base = r[0] + 'ائ' + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ائ';
	else :
		base_n = r[0] + 'ائ' + r[2];


	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));
	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{

		base = r[0] + 'اء' + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + 'اء';
		else :
			base_n = r[0] + 'اء' + r[2];

		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}



def secondhamza_patt3_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs('م' + r[0] + 'ائ' + r[2], '-');
#}


def secondhamza_patt3_pp(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pp('م' + r[0] + 'اء' + r[2], '-');
#}


## ----------------------------------------------------------------------------##
## pattern 4
## ----------------------------------------------------------------------------##


def secondhamza_patt4_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[0] + 'أ' + r[2];

	if r[2] == 'ت' :
		base_t = 'أ' + r[0] + 'أ';
	else :
		base_t = 'أ' + r[0] + 'أ' + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[0] + 'أ';
	else :
		base_n = 'أ' + r[0] + 'أ' + r[2];

	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'أ' + r[0] + 'ئ' + r[2];

		if r[2] == 'ت' :
			base_t = 'أ' + r[0] + 'ئ';
		else :
			base_t = 'أ' + r[0] + 'ئ' + r[2];

		if r[2] == 'ن' :
			base_n = 'أ' + r[0] + 'ئ';
		else :
			base_n = 'أ' + r[0] + 'ئ' + r[2];
		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def secondhamza_patt4_pres(root, tv): #{
	r = root.split('-'); # radicals

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';


	base = r[0] + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ئ';
	else :
		base_n = r[0] + 'ئ' + r[2];


	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));

	base = 'أ' + r[0] + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[0] + 'ئ';
	else :
		base_n = 'أ' + r[0] + 'ئ' + r[2];

	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{

		base = r[0] + 'أ' + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + 'أ';
		else :
			base_n = r[0] + 'أ' + r[2];

		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}


	return forms;
#}


def secondhamza_patt4_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs('م' + r[0] + 'ئ' + r[2], '-');
#}


def secondhamza_patt4_pp(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pp('م' + r[0] + 'أ' + r[2], '-');
#}


## ----------------------------------------------------------------------------##
## pattern 5
## ----------------------------------------------------------------------------##


def secondhamza_patt5_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'أ' + r[2];

	if r[2] == 'ت' :
		base_t = 'ت' + r[0] + 'أ';
	else :
		base_t = 'ت' + r[0] + 'أ' + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'أ';
	else :
		base_n = 'ت' + r[0] + 'أ' + r[2];

	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'ت' + r[0] + 'ئ' + r[2];

		if r[2] == 'ت' :
			base_t = 'ت' + r[0] + 'ئ';
		else :
			base_t = 'ت' + r[0] + 'ئ' + r[2];

		if r[2] == 'ن' :
			base_n = 'ت' + r[0] + 'ئ';
		else :
			base_n = 'ت' + r[0] + 'ئ' + r[2];

		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def secondhamza_patt5_pres(root, tv): #{
	r = root.split('-'); # radicals

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';


	base = 'ت' + r[0] + 'أ' + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'أ';
	else :
		base_n = 'ت' + r[0] + 'أ' + r[2];


	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));
	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{
		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def secondhamza_patt5_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs('مت' + r[0] + 'ئ' + r[2], '-');
#}


# rare
def secondhamza_patt5_pp(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pp('مت' + r[0] + 'أ' + r[2], '-');
#}


## ----------------------------------------------------------------------------##
## pattern 6
## ----------------------------------------------------------------------------##


def secondhamza_patt6_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'اء' + r[2];

	if r[2] == 'ت' :
		base_t = 'ت' + r[0] + 'اء';
	else :
		base_t = 'ت' + r[0] + 'اء' + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'اء';
	else :
		base_n = 'ت' + r[0] + 'اء' + r[2];

	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'ت' + r[0] + 'وئ' + r[2];

		if r[2] == 'ت' :
			base_t = 'ت' + r[0] + 'وئ';
		else :
			base_t = 'ت' + r[0] + 'وئ' + r[2];

		if r[2] == 'ن' :
			base_n = 'ت' + r[0] + 'وئ';
		else :
			base_n = 'ت' + r[0] + 'وئ' + r[2];

		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def secondhamza_patt6_pres(root, tv): #{
	r = root.split('-'); # radicals

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';


	base = 'ت' + r[0] + 'اء' + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'اء';
	else :
		base_n = 'ت' + r[0] + 'اء' + r[2];


	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));
	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{
		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def secondhamza_patt6_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs('مت' + r[0] + 'ائ' + r[2], '-');
#}


def secondhamza_patt6_pp(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pp('مت' + r[0] + 'اء' + r[2], '-');
#}


## ----------------------------------------------------------------------------##
## pattern 7
## ----------------------------------------------------------------------------##


def secondhamza_patt7_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ان' + r[0] + 'أ' + r[2];

	if r[2] == 'ت' :
		base_t = 'ان' + r[0] + 'أ';
	else :
		base_t = 'ان' + r[0] + 'أ' + r[2];

	if r[2] == 'ن' :
		base_n = 'ان' + r[0] + 'أ';
	else :
		base_n = 'ان' + r[0] + 'أ' + r[2];

	return secondhamza_past_actv(base, base_t, base_n, tv);

	return forms;
#}


def secondhamza_patt7_pres(root, tv): #{
	r = root.split('-'); # radicals

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';


	base = 'ن' + r[0] + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = 'ن' + r[0] + 'ئ';
	else :
		base_n = 'ن' + r[0] + 'ئ' + r[2];

	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));

	base = 'ان' + r[0] + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = 'ان' + r[0] + 'ئ';
	else :
		base_n = 'ان' + r[0] + 'ئ' + r[2];

	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	return forms;

#}


def secondhamza_patt7_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs('من' + r[0] + 'ئ' + r[2], '-');
#}


## ----------------------------------------------------------------------------##
## pattern 8
## ----------------------------------------------------------------------------##


def secondhamza_patt8_past(root, tv): #{
	r = root.split('-'); # radicals

	base_start = 'ا' + r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = 'ا' + r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = 'ا' + r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = 'ا' + r[0] + 'د';
	
	base = base_start + 'أ' + r[2];

	if r[2] == 'ت' :
		base_t = base_start + 'أ';
	else :
		base_t = base_start + 'أ' + r[2];

	if r[2] == 'ن' :
		base_n = base_start + 'أ';
	else :
		base_n = base_start + 'أ' + r[2];


	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = base_start + 'ئ' + r[2];

		if r[2] == 'ت' :
			base_t = base_start + 'ئ';
		else :
			base_t = base_start + 'ئ' + r[2];

		if r[2] == 'ن' :
			base_n = base_start + 'ئ';
		else :
			base_n = base_start + 'ئ' + r[2];

		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def secondhamza_patt8_pres(root, tv): #{
	r = root.split('-'); # radicals

	base_start = r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = r[0] + 'د';
	
	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';


	base = base_start + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = base_start + 'ئ';
	else :
		base_n = base_start + 'ئ' + r[2];


	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));

	base = 'ا' + base_start + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = 'ا' + base_start + 'ئ';
	else :
		base_n = 'ا' + base_start + 'ئ' + r[2];

	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{
		base = base_start + 'أ' + r[2];

		if r[2] == 'ن' :
			base_n = base_start + 'أ';
		else :
			base_n = base_start + 'أ' + r[2];

		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}

	return forms;

#}


def secondhamza_patt8_pprs(root): #{
	r = root.split('-'); # radicals

	base = r[0] + 'تئ' + r[2];
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base = r[0] + 'ئ' + r[2];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base = r[0] + 'طئ' + r[2];
	elif (r[0] == 'ز') :
		base = r[0] + 'دئ' + r[2];

	return secondhamza_pprs('م' + base, '-');
#}


def secondhamza_patt8_pp(root): #{
	r = root.split('-'); # radicals

	base = r[0] + 'تأ' + r[2];
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base = r[0] + 'أ' + r[2];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base = r[0] + 'طأ' + r[2];
	elif (r[0] == 'ز') :
		base = r[0] + 'دأ' + r[2];

	return secondhamza_pp('م' + base, '-');
#}



## ----------------------------------------------------------------------------##
## pattern 10
## ----------------------------------------------------------------------------##


def secondhamza_patt10_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'است' + r[0] + 'أ' + r[2];

	if r[2] == 'ت' :
		base_t = 'است' + r[0] + 'أ';
	else :
		base_t = 'است' + r[0] + 'أ' + r[2];

	if r[2] == 'ن' :
		base_n = 'است' + r[0] + 'أ';
	else :
		base_n = 'است' + r[0] + 'أ' + r[2];

	forms = secondhamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'است' + r[0] + 'ئ' + r[2];

		if r[2] == 'ت' :
			base_t = 'است' + r[0] + 'ئ';
		else :
			base_t = 'است' + r[0] + 'ئ' + r[2];

		if r[2] == 'ن' :
			base_n = 'است' + r[0] + 'ئ';
		else :
			base_n = 'است' + r[0] + 'ئ' + r[2];

		forms.update(secondhamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def secondhamza_patt10_pres(root, tv): #{
	r = root.split('-'); # radicals

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';


	base = 'ست' + r[0] + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = 'ست' + r[0] + 'ئ';
	else :
		base_n = 'ست' + r[0] + 'ئ' + r[2];


	forms = secondhamza_pres_actv(base, base_n, tv);
	forms.update(secondhamza_subjun_actv(base, base_n, subtype, tv));
	forms.update(secondhamza_apocop_actv(base, base_n, tv));

	base = 'است' + r[0] + 'ئ' + r[2];

	if r[2] == 'ن' :
		base_n = 'است' + r[0] + 'ئ';
	else :
		base_n = 'است' + r[0] + 'ئ' + r[2];

	forms.update(secondhamza_imp(base, base_n, subtype, tv));

	if (tv == 'tv') : #{

		base = 'ست' + r[0] + 'أ' + r[2];

		if r[2] == 'ن' :
			base_n = 'ست' + r[0] + 'أ';
		else :
			base_n = 'ست' + r[0] + 'أ' + r[2];

		forms.update(secondhamza_subjun_pasv(base, base_n));
		forms.update(secondhamza_pres_pasv(base, base_n));
		forms.update(secondhamza_apocop_pasv(base, base_n));
	#}


	return forms;
#}


def secondhamza_patt10_pprs(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pprs('مست' + r[0] + 'ئ' + r[2], '-');
#}


def secondhamza_patt10_pp(root): #{
	r = root.split('-'); # radicals

	return secondhamza_pp('مست' + r[0] + 'أ' + r[2], '-');
#}



## ----------------------------------------------------------------------------##
## main
## ----------------------------------------------------------------------------##


def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{
		forms.update(secondhamza_patt1_past(stem['root'], stem['vowels_perf'], stem['trans']));
		forms.update(secondhamza_patt1_pres(stem['root'], stem['vowels_impf'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt1_pp(stem['root']));
		forms.update(secondhamza_patt1_pprs(stem['root']));
	#}
	elif stem['theme'] == '2' : #{
		forms.update(secondhamza_patt2_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt2_pres(stem['root'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt2_pp(stem['root']));
		forms.update(secondhamza_patt2_pprs(stem['root']));
	#}
	elif stem['theme'] == '3' : #{
		forms.update(secondhamza_patt3_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt3_pres(stem['root'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt3_pp(stem['root']));
		forms.update(secondhamza_patt3_pprs(stem['root']));
	#}
	elif stem['theme'] == '4' : #{
		forms.update(secondhamza_patt4_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt4_pres(stem['root'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt4_pp(stem['root']));
		forms.update(secondhamza_patt4_pprs(stem['root']));
	#}
	elif stem['theme'] == '5' : #{
		forms.update(secondhamza_patt5_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt5_pres(stem['root'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt5_pp(stem['root']));
		forms.update(secondhamza_patt5_pprs(stem['root']));
	#}
	elif stem['theme'] == '6' : #{
		forms.update(secondhamza_patt6_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt6_pres(stem['root'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt6_pp(stem['root']));
		forms.update(secondhamza_patt6_pprs(stem['root']));
	#}
	elif stem['theme'] == '7' : #{
		forms.update(secondhamza_patt7_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt7_pres(stem['root'], stem['trans']));
		forms.update(secondhamza_patt7_pprs(stem['root']));
	#}
	elif stem['theme'] == '8' : #{
		forms.update(secondhamza_patt8_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt8_pres(stem['root'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt8_pp(stem['root']));
		forms.update(secondhamza_patt8_pprs(stem['root']));
	#}
	elif stem['theme'] == '10' : #{
		forms.update(secondhamza_patt10_past(stem['root'], stem['trans']));
		forms.update(secondhamza_patt10_pres(stem['root'], stem['trans']));
                if stem['trans'] == 'tv':
			forms.update(secondhamza_patt10_pp(stem['root']));
		forms.update(secondhamza_patt10_pprs(stem['root']));
	#}

	return forms;

#}

