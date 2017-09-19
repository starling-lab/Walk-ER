import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 24})

def update_figures(domain, Y_label, ylim=[], ytick_labels=[]):

    name_to_save = 'graphs/' + (domain + Y_label).replace(' ','') + '.png'

    global t0
    global t1
    global t2
    global t3
    global t4

    global t0error
    global t1error
    global t2error
    global t3error
    global t4error

    fig = plt.figure()
    axes = plt.gca()
    
    if domain == 'Cora':
        x = range(7)[1:]
    elif domain == 'IMDB':
        x = range(5)[1:]
    elif domain == 'WebKB':
        x = range(5)[1:]
    elif domain == 'CiteSeer':
        x = range(15)[1:]
    elif domain == 'UW-CSE':
        x = range(15)[1:]

    if ylim:
        axes.set_ylim(ylim)

    if ytick_labels:
        plt.yticks(ytick_labels[0], ytick_labels[1])
    
    #axes.set_ylim([0.2, 1.0])
    plt.xticks(x, x)

    (_, caps, _) = plt.errorbar(1, t0[0], yerr=t0error[0], fmt='co', capsize=20, elinewidth=6, label='Gold Standard') # Tushar
    for cap in caps:
        cap.set_markeredgewidth(2)

    #(_, caps, _) = plt.errorbar(1, t1[0], yerr=t1error[0], fmt='co', capsize=20, elinewidth=6, label='Walk Everywhere') # -e
    #for cap in caps:
    #    cap.set_markeredgewidth(2)

    (_, caps, _) = plt.errorbar(x, t2, yerr=t2error, fmt='r-o', capsize=20, linewidth=4, elinewidth=4, label='Random Walk') # -rw
    for cap in caps:
        cap.set_markeredgewidth(2)

    (_, caps, _) = plt.errorbar(x, t3, yerr=t3error, fmt='b-o', capsize=20, linewidth=4, elinewidth=4, label='Walk All Paths') # -w
    for cap in caps:
        cap.set_markeredgewidth(2)

    (_, caps, _) = plt.errorbar(x, t4, yerr=t4error, fmt='g-o', capsize=20, linewidth=4, elinewidth=4, label='Walk Shortest Path') # -s
    for cap in caps:
        cap.set_markeredgewidth(2)

    #plt.title('IMDB: Avg. Training Time vs. Number of Predicates')
    plt.xlabel('Number of Predicates')
    plt.ylabel(Y_label)
    plt.tight_layout()
    
    #plt.show()
    #plt.legend()
    plt.savefig(name_to_save, bbox_inches='tight')


aucrocmargins = [0.35, 1.0]
aucprmargins = [0.0, 1.0]

# Training Time: CiteSeer
t0 = [np.mean([48733.566, 5273.227, 54623.805, 40455.021])]
t1 = [np.mean([3837.157, 3141.227, 5773.856, 7600.662])]
t2 = [66.294499999999999, 66.003, 129.26837499999999, 83.831625000000003, 3807.6718750000005, 4459.2172499999997, 1941.6811250000001, 3707.4506249999999, 9777.5106250000008, 9295.2962499999994, 15222.17525, 9412.2760000000017, 55419.861124999999, 22192.613499999999]
t3 = [152.29750000000001, 759.25275000000011, 834.27224999999999, 776.63350000000003, 713.24824999999998, 662.17225000000008, 6033.4675000000007, 5100.8027500000007, 5109.3464999999997, 5438.9757499999996, 5345.2049999999999, 5107.1144999999997, 6185.2420000000002, 5635.3989999999994]
t4 = [152.773, 190.56274999999999, 191.15674999999999, 189.75624999999999, 191.01525000000001, 193.38675000000001, 5209.1307500000003, 4851.0510000000004, 4132.6677499999996, 3497.1219999999998, 5095.9027499999993, 4855.2222499999998, 4301.9262500000004, 4384.741]

t0error = [np.std([48733.566, 5273.227, 54623.805, 40455.021])]
t1error = [np.std([3837.157, 3141.227, 5773.856, 7600.662])]
t2error = [11.210294420754522, 10.926739266588182, 40.475938691824986, 32.048382845073093, 8799.1742464687486, 8532.7164139113956, 2995.6092432165797, 5231.802472169079, 11237.950714655062, 17390.197938219389, 21793.842003392077, 9774.8009648679945, 100696.46674057224, 13555.483158946228]
t3error = [23.80844661564462, 118.57813524080859, 101.82531164787811, 123.83055609279158, 101.96089920742905, 123.62782357822003, 616.8670550339433, 445.11045677526795, 975.73523599809073, 1642.5842844933979, 2401.8632439777871, 1479.4318661211639, 1529.696766576958, 869.0911117900697]
t4error = [16.493532232363087, 27.893267605060192, 20.407644858912548, 25.014516079418769, 19.504431449993614, 20.575188654967416, 439.54878005710299, 452.48191294956729, 1551.8559868243854, 406.58569212221425, 1445.6040632533816, 988.35707879525398, 1245.9458288596206, 1528.060034569977]

update_figures('CiteSeer', 'Average Training Time (s)', ylim=[0, 60000], ytick_labels=[[0, 10000, 20000, 30000, 40000, 50000, 60000], ['0', '10k', '20k', '30k', '40k', '50k', '60k']])

# CiteSeer AUC ROC scores
t0 = [np.mean([0.86008600000000002, 0.86646699999999999, 0.85475950000000001, 0.96288649999999998])]
t1 = [np.mean([0.795613, 0.811597, 0.819605, 0.967054])]
t2 = [0.5, 0.5, 0.65086575000000002, 0.55039700000000003, 0.68886562500000004, 0.68603175000000005, 0.69469124999999998, 0.73169862500000005, 0.78259649999999992, 0.79928650000000001, 0.81104949999999998, 0.78027499999999994, 0.80258750000000001, 0.86569474999999996]
t3 = [0.70562174999999994, 0.76466374999999998, 0.76558900000000008, 0.76526075000000005, 0.76539924999999998, 0.76365075000000004, 0.81408349999999996, 0.80808075000000001, 0.90233174999999999, 0.86373100000000003, 0.91461250000000005, 0.87507025000000005, 0.90653950000000005, 0.91006749999999992]
t4 = [0.70553825000000003, 0.74286399999999997, 0.73907650000000003, 0.7439635, 0.74421225000000002, 0.74416024999999997, 0.80766700000000002, 0.83386300000000002, 0.90936800000000007, 0.81772049999999996, 0.90397050000000001, 0.87065799999999993, 0.88253474999999992, 0.87501874999999996]

t0error = [np.std([0.86008600000000002, 0.86646699999999999, 0.85475950000000001, 0.96288649999999998])]
t1error = [np.std([0.795613, 0.811597, 0.819605, 0.967054])]
t2error = [0.0, 0.0, 0.088301250208802251, 0.087380533049415537, 0.074907896005590585, 0.072570053749377222, 0.12743589684401135, 0.15311498667744569, 0.094929031474833891, 0.081637478464244587, 0.076153576736421244, 0.071312099530865022, 0.083072726977630865, 0.057260482439353395]
t3error = [0.014475448341502231, 0.010918384069426197, 0.012152375426228408, 0.012460115356107264, 0.012129552740620749, 0.012474005198311376, 0.012304109079896824, 0.011449642841045323, 0.05156756820122025, 0.053569763976519441, 0.057892513287557304, 0.069150490079156343, 0.051017855082804084, 0.053077123925943832]
t4error = [0.014533757899714039, 0.01584084483226824, 0.01995234310175124, 0.015500108620587155, 0.015397313050902743, 0.015931249282071371, 0.01375777576499923, 0.064405169093792458, 0.059639559761118253, 0.015330522194302431, 0.059570205545641686, 0.059396697100933163, 0.070644406743828644, 0.057164019270757177]

update_figures('CiteSeer', 'Average AUC ROC', ylim=aucrocmargins)

# CiteSeer AUC PR Scores
t0 = [np.mean([0.856427, 0.829349, 0.777146, 0.922103, 0.651146, 0.654548, 0.644997, 0.924747])]
t1 = [np.mean([0.651146, 0.654548, 0.644997, 0.924747])]
t2 = [0.31054775000000001, 0.31054775000000001, 0.46190162499999998, 0.36085487500000002, 0.50541237500000002, 0.49681162499999998, 0.52267924999999993, 0.578928, 0.64097100000000007, 0.65155437500000002, 0.669245125, 0.61958987499999996, 0.66927512499999997, 0.75959250000000011]
t3 = [0.51612650000000004, 0.56903399999999993, 0.57008725000000005, 0.56993450000000001, 0.57024525000000004, 0.56723699999999999, 0.65799649999999998, 0.64810349999999994, 0.80223499999999992, 0.73478474999999999, 0.82352650000000005, 0.75974549999999996, 0.80803075000000002, 0.81298274999999998]
t4 = [0.51580575000000006, 0.54927175000000006, 0.54545624999999998, 0.55072925000000006, 0.55164975000000005, 0.55075825, 0.64594949999999995, 0.68935524999999997, 0.81166175000000007, 0.66356999999999999, 0.79817875000000005, 0.75475599999999998, 0.76780349999999997, 0.76394725000000008]

t0error = [np.std([0.856427, 0.829349, 0.777146, 0.922103, 0.651146, 0.654548, 0.644997, 0.924747])]
t1error = [np.std([0.651146, 0.654548, 0.644997, 0.924747])]
t2error = [0.019148175675178555, 0.019148175675178555, 0.086093824202055136, 0.080194105773799693, 0.078068794647633541, 0.065820823015853985, 0.14482029249189321, 0.18666209228241817, 0.14505453505492341, 0.11004467798914391, 0.12209165043158918, 0.097765514669587744, 0.12413366628098671, 0.086016775028188552]
t3error = [0.021037452941123833, 0.022020521599181067, 0.023052268449927013, 0.023643862940518002, 0.02315052220118374, 0.022611706713558812, 0.021498641172176418, 0.021296624503662556, 0.088062666346187854, 0.075608742448790248, 0.11247879055737574, 0.11959136575125313, 0.097422363752823718, 0.10038725200286887]
t4error = [0.02120360851806834, 0.025348786158068817, 0.026952600351125688, 0.025445429043101271, 0.024847906666105694, 0.025752348517902215, 0.025335623127328077, 0.10868550198709807, 0.11465349974461095, 0.021385337324905596, 0.11467623641665042, 0.089740580898498762, 0.12733247965169767, 0.087208642623237173]

update_figures('CiteSeer', 'Average AUC PR', ylim=aucprmargins)

# WebKB Training Times
t0 = [np.mean([3.834, 3.435, 3.573, 3.701, 3.408, 3.577, 2.924, 2.821, 4.173, 3.554, 3.542, 3.657, 3.679, 3.817, 2.94, 3.087, 3.385, 2.915, 3.155, 4.252, 3.475, 3.537, 3.083, 3.016, 3.802, 4.22, 2.378, 2.896, 2.602, 4.016, 2.453, 3.601, 3.05, 3.943, 2.731, 2.841, 3.968, 3.569, 3.397, 4.027])]
t1 = [np.mean([2.111, 2.918, 2.815, 2.574, 2.835, 2.075, 3.224, 3.035, 3.13, 2.86, 2.734, 3.147, 3.038, 2.954, 2.638, 2.821, 3.039, 2.936, 2.584, 2.823, 2.023, 2.59, 2.765, 2.621, 2.705, 2.737, 2.719, 3.265, 2.726, 2.736, 2.511, 2.849, 2.767, 2.713, 2.319, 3.176, 3.195, 2.708, 2.384, 2.998])]
t2 = [2.1901875, 2.1725124999999998, 2.4612875000000001, 2.5109625000000002]
t3 = [2.7441750000000003, 2.7967249999999999, 2.7914000000000003, 2.9151499999999997]
t4 = [2.4994500000000004, 2.4888249999999998, 2.872725, 2.8693]

t0error = [np.std([3.834, 3.435, 3.573, 3.701, 3.408, 3.577, 2.924, 2.821, 4.173, 3.554, 3.542, 3.657, 3.679, 3.817, 2.94, 3.087, 3.385, 2.915, 3.155, 4.252, 3.475, 3.537, 3.083, 3.016, 3.802, 4.22, 2.378, 2.896, 2.602, 4.016, 2.453, 3.601, 3.05, 3.943, 2.731, 2.841, 3.968, 3.569, 3.397, 4.027])]
t1error = [np.std([2.111, 2.918, 2.815, 2.574, 2.835, 2.075, 3.224, 3.035, 3.13, 2.86, 2.734, 3.147, 3.038, 2.954, 2.638, 2.821, 3.039, 2.936, 2.584, 2.823, 2.023, 2.59, 2.765, 2.621, 2.705, 2.737, 2.719, 3.265, 2.726, 2.736, 2.511, 2.849, 2.767, 2.713, 2.319, 3.176, 3.195, 2.708, 2.384, 2.998])]
t2error = [0.19855270671474112, 0.19247759569297929, 0.22732796757933241, 0.25158787946510858]
t3error = [0.26624386260531907, 0.27729226346041463, 0.28669816881173132, 0.20332935720156103]
t4error = [0.20212050242367796, 0.24429059411897136, 0.25212100145565031, 0.26195774468413791]

update_figures('WebKB', 'Average Training Time (s)')

# WebKB AUC ROC
t0 = [np.mean([0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.691485, 0.855079, 0.67705, 0.838965, 0.691485, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.67705, 0.838965, 0.693953, 0.855079])]
t1 = [np.mean([0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681])]
t2 = [0.52964725000000001, 0.52964725000000001, 0.58581121250000012, 0.56027142500000005]
t3 = [0.77431850000000002, 0.77444190000000002, 0.77425680000000008, 0.77419510000000002]
t4 = [0.7442323500000001, 0.7442323500000001, 0.77438020000000007, 0.77419510000000002]

t0error = [np.std([0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.712358, 0.838965, 0.691485, 0.855079, 0.67705, 0.838965, 0.691485, 0.855079, 0.712358, 0.838965, 0.693953, 0.855079, 0.67705, 0.838965, 0.693953, 0.855079])]
t1error = [np.std([0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.714932, 0.855681, 0.694704, 0.833191, 0.712464, 0.855681])]
t2error = [0.017478188312508258, 0.017478188312508258, 0.095427450746718281, 0.067651108254369152]
t3error = [0.070888405344245134, 0.070782693119787424, 0.070941121890339465, 0.070993745668826366]
t4error = [0.065449227602986271, 0.065449227602986271, 0.070835595823427661, 0.070993745668826366]

update_figures('WebKB', 'Average AUC ROC', ylim=aucrocmargins)

# WebKB AUC PR
t0 = [np.mean([0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.49937, 0.78304, 0.562044, 0.727559, 0.49937, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.562044, 0.727559, 0.54979, 0.78304])]
t1 = [np.mean([0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489])]
t2 = [0.21414074999999996, 0.21414074999999996, 0.31478658749999999, 0.26465976250000001]
t3 = [0.65426074999999995, 0.65678174999999994, 0.65300025000000006, 0.65173974999999995]
t4 = [0.64371749999999994, 0.64371749999999994, 0.65552124999999994, 0.65173974999999995]

t0error = [np.std([0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.586154, 0.727559, 0.49937, 0.78304, 0.562044, 0.727559, 0.49937, 0.78304, 0.586154, 0.727559, 0.54979, 0.78304, 0.562044, 0.727559, 0.54979, 0.78304])]
t1error = [np.std([0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.55997, 0.783489, 0.57579, 0.723004, 0.50955, 0.783489])]
t2error = [0.014391817125974744, 0.014391817125974744, 0.1847780022539002, 0.12765621080290648]
t3error = [0.10307667895158196, 0.10007958593633119, 0.10452020988396216, 0.10592907572610789]
t4error = [0.095156491619069278, 0.095156491619069278, 0.10159700533326511, 0.10592907572610789]

update_figures('WebKB', 'Average AUC PR', ylim=aucprmargins)

# Cora Training Times
t0 = [np.mean([395.158, 33.093, 66.425, 149.923, 218.648, 406.36, 118.124, 70.747, 172.855, 235.423, 400.348, 123.477, 71.319, 148.331, 209.6, 303.451, 148.737, 66.375, 158.138, 244.382, 261.983, 138.625, 62.091, 240.901, 207.684, 378.212, 127.303, 170.96699999999998, 152.327, 219.21800000000002, 474.28499999999997, 134.223, 69.352, 271.379, 152.81799999999998, 343.719, 137.225, 61.772, 182.503, 252.019, 408.993, 183.69, 64.545, 181.963, 157.848, 397.448, 126.528, 59.859, 209.612, 141.385])]
t1 = [np.mean([213.986, 190.615, 49.046, 126.841, 224.625, 202.17000000000002, 123.571, 58.287, 124.848, 226.16899999999998, 244.703, 148.059, 54.44, 119.275, 172.007, 376.444, 134.439, 83.339, 130.804, 154.152, 203.567, 135.83, 52.772, 127.105, 177.53199999999998, 207.414, 141.594, 51.194, 118.923, 210.93, 250.865, 175.59199999999998, 70.05799999999999, 122.936, 165.132, 405.884, 124.083, 51.211, 145.596, 266.537, 240.877, 126.123, 54.508, 143.95, 236.965, 230.097, 131.329, 59.252, 134.466, 244.613])]
t2 = [2.0954300000000003, 2.1603599999999998, 3.5576300000000005, 3.12378, 9.3047699999999978, 6.7222299999999997]
t3 = [147.22794000000002, 165.92644000000001, 148.16513999999998, 154.17408, 151.66983999999999, 151.06618]
t4 = [4.6962200000000003, 8.4916, 8.8706599999999991, 75.898219999999995, 139.31299999999999, 151.60712000000001]

t0error = [np.std([395.158, 33.093, 66.425, 149.923, 218.648, 406.36, 118.124, 70.747, 172.855, 235.423, 400.348, 123.477, 71.319, 148.331, 209.6, 303.451, 148.737, 66.375, 158.138, 244.382, 261.983, 138.625, 62.091, 240.901, 207.684, 378.212, 127.303, 170.96699999999998, 152.327, 219.21800000000002, 474.28499999999997, 134.223, 69.352, 271.379, 152.81799999999998, 343.719, 137.225, 61.772, 182.503, 252.019, 408.993, 183.69, 64.545, 181.963, 157.848, 397.448, 126.528, 59.859, 209.612, 141.385])]
t1error = [np.std([213.986, 190.615, 49.046, 126.841, 224.625, 202.17000000000002, 123.571, 58.287, 124.848, 226.16899999999998, 244.703, 148.059, 54.44, 119.275, 172.007, 376.444, 134.439, 83.339, 130.804, 154.152, 203.567, 135.83, 52.772, 127.105, 177.53199999999998, 207.414, 141.594, 51.194, 118.923, 210.93, 250.865, 175.59199999999998, 70.05799999999999, 122.936, 165.132, 405.884, 124.083, 51.211, 145.596, 266.537, 240.877, 126.123, 54.508, 143.95, 236.965, 230.097, 131.329, 59.252, 134.466, 244.613])]
t2error = [0.25835608198763194, 0.28515699254971816, 1.3659084936773767, 1.2743825138473928, 20.606148525066487, 12.515120539455463]
t3error = [79.537726863523062, 86.345986133962242, 64.129672500960112, 72.007726260683995, 71.778009009824174, 75.799684638576167]
t4error = [0.49842790010191046, 1.5387074835718451, 1.530861386409625, 39.600749561739356, 69.071654957442561, 84.440184800754679]

update_figures('Cora', 'Average Training Time (s)', ylim=[0, 350])

# Cora AUC ROC
t0 = [np.mean([0.837321, 0.422131, 0.483444, 0.740506, 0.573966, 0.837321, 0.389344, 0.633278, 0.740506, 0.555556, 0.861244, 0.422131, 0.483444, 0.740506, 0.596899, 0.851675, 0.41127, 0.483444, 0.740506, 0.653747, 0.837321, 0.389344, 0.491722, 0.742089, 0.570413, 0.851675, 0.41127, 0.610099, 0.742089, 0.589793, 0.866029, 0.389344, 0.483444, 0.740506, 0.523579, 0.851675, 0.389344, 0.483444, 0.742089, 0.596899, 0.866029, 0.389344, 0.483444, 0.740506, 0.601421, 0.866029, 0.389344, 0.491722, 0.740506, 0.555556])]
t1 = [np.mean([0.837321, 0.389344, 0.491722, 0.740506, 0.598837, 0.837321, 0.355533, 0.483444, 0.740506, 0.574935, 0.837321, 0.389344, 0.491722, 0.740506, 0.565245, 0.837321, 0.389344, 0.610099, 0.740506, 0.626292, 0.837321, 0.41127, 0.491722, 0.740506, 0.548127, 0.837321, 0.329508, 0.491722, 0.740506, 0.635013, 0.837321, 0.389344, 0.483444, 0.740506, 0.534884, 0.837321, 0.389344, 0.486755, 0.740506, 0.614987, 0.837321, 0.389344, 0.483444, 0.742089, 0.597222, 0.837321, 0.389344, 0.821192, 0.740506, 0.573966])]
t2 = [0.5, 0.5, 0.52000002000000001, 0.51666668000000004, 0.53304656000000006, 0.53831421000000002]
t3 = [0.60712842, 0.61374901999999987, 0.60683297999999997, 0.61867968000000007, 0.61907224000000005, 0.61105273999999998]
t4 = [0.5, 0.5833334, 0.5833334, 0.55018592000000011, 0.60476997999999993, 0.61034429999999995]

t0error = [np.std([0.837321, 0.422131, 0.483444, 0.740506, 0.573966, 0.837321, 0.389344, 0.633278, 0.740506, 0.555556, 0.861244, 0.422131, 0.483444, 0.740506, 0.596899, 0.851675, 0.41127, 0.483444, 0.740506, 0.653747, 0.837321, 0.389344, 0.491722, 0.742089, 0.570413, 0.851675, 0.41127, 0.610099, 0.742089, 0.589793, 0.866029, 0.389344, 0.483444, 0.740506, 0.523579, 0.851675, 0.389344, 0.483444, 0.742089, 0.596899, 0.866029, 0.389344, 0.483444, 0.740506, 0.601421, 0.866029, 0.389344, 0.491722, 0.740506, 0.555556])]
t1error = [np.std([0.837321, 0.389344, 0.491722, 0.740506, 0.598837, 0.837321, 0.355533, 0.483444, 0.740506, 0.574935, 0.837321, 0.389344, 0.491722, 0.740506, 0.565245, 0.837321, 0.389344, 0.610099, 0.740506, 0.626292, 0.837321, 0.41127, 0.491722, 0.740506, 0.548127, 0.837321, 0.329508, 0.491722, 0.740506, 0.635013, 0.837321, 0.389344, 0.483444, 0.740506, 0.534884, 0.837321, 0.389344, 0.486755, 0.740506, 0.614987, 0.837321, 0.389344, 0.483444, 0.742089, 0.597222, 0.837321, 0.389344, 0.821192, 0.740506, 0.573966])]
t2error = [0.0, 0.0, 0.06137322326014498, 0.057735061560005289, 0.11047990629506525, 0.093371609261412539]
t3error = [0.162643211176869, 0.16111663358815437, 0.16781023107933435, 0.16358854132932904, 0.16155143257768531, 0.16573405599994348]
t4error = [0.0, 0.1054093080436448, 0.1054093080436448, 0.18833580422583909, 0.16316070077435804, 0.16416818247666018]

update_figures('Cora', 'Average AUC ROC', ylim=aucrocmargins)

# Cora AUC PR
t0 = [np.mean([0.986643, 0.851625, 0.954354, 0.915654, 0.905988, 0.986643, 0.830003, 0.969379, 0.915654, 0.90206, 0.988828, 0.851625, 0.954354, 0.915654, 0.940777, 0.987965, 0.830251, 0.954354, 0.915654, 0.950035, 0.986643, 0.830003, 0.958321, 0.917486, 0.90366, 0.987965, 0.830251, 0.968389, 0.917486, 0.921909, 0.989255, 0.830003, 0.954354, 0.915654, 0.896631, 0.987965, 0.830003, 0.954354, 0.917486, 0.929398, 0.989255, 0.830003, 0.954354, 0.915654, 0.94126, 0.989255, 0.830003, 0.958321, 0.915654, 0.90206])]
t1 = [np.mean([0.986643, 0.830003, 0.958321, 0.915654, 0.925205, 0.986643, 0.804728, 0.954354, 0.915654, 0.905811, 0.986643, 0.830003, 0.958321, 0.915654, 0.903377, 0.986643, 0.830003, 0.968389, 0.915654, 0.945032, 0.986643, 0.830251, 0.958321, 0.915654, 0.900474, 0.986643, 0.780417, 0.958321, 0.915654, 0.927967, 0.986643, 0.830003, 0.954354, 0.915654, 0.89853, 0.986643, 0.830003, 0.958181, 0.915654, 0.943758, 0.986643, 0.830003, 0.954354, 0.917486, 0.910402, 0.986643, 0.830003, 0.994615, 0.915654, 0.907061])]
t2 = [0.91510940000000007, 0.91510940000000007, 0.91863104000000007, 0.91804063999999996, 0.92201314000000001, 0.92222524000000006]
t3 = [0.92086144000000014, 0.92279697999999977, 0.92052953999999998, 0.92481888000000012, 0.92342429999999998, 0.92129915999999989]
t4 = [0.91510939999999996, 0.92976560000000008, 0.92976560000000008, 0.93737481999999983, 0.92063116000000023, 0.92323494000000006]

t0error = [np.std([0.986643, 0.851625, 0.954354, 0.915654, 0.905988, 0.986643, 0.830003, 0.969379, 0.915654, 0.90206, 0.988828, 0.851625, 0.954354, 0.915654, 0.940777, 0.987965, 0.830251, 0.954354, 0.915654, 0.950035, 0.986643, 0.830003, 0.958321, 0.917486, 0.90366, 0.987965, 0.830251, 0.968389, 0.917486, 0.921909, 0.989255, 0.830003, 0.954354, 0.915654, 0.896631, 0.987965, 0.830003, 0.954354, 0.917486, 0.929398, 0.989255, 0.830003, 0.954354, 0.915654, 0.94126, 0.989255, 0.830003, 0.958321, 0.915654, 0.90206])]
t1error = [np.std([0.986643, 0.830003, 0.958321, 0.915654, 0.925205, 0.986643, 0.804728, 0.954354, 0.915654, 0.905811, 0.986643, 0.830003, 0.958321, 0.915654, 0.903377, 0.986643, 0.830003, 0.968389, 0.915654, 0.945032, 0.986643, 0.830251, 0.958321, 0.915654, 0.900474, 0.986643, 0.780417, 0.958321, 0.915654, 0.927967, 0.986643, 0.830003, 0.954354, 0.915654, 0.89853, 0.986643, 0.830003, 0.958181, 0.915654, 0.943758, 0.986643, 0.830003, 0.954354, 0.917486, 0.910402, 0.986643, 0.830003, 0.994615, 0.915654, 0.907061])]
t2error = [0.037305778172288535, 0.037305778172288535, 0.038060451421894612, 0.038034270913353915, 0.038542505577095008, 0.038687760971428668]
t3error = [0.053354925603981501, 0.051153444592711449, 0.055665851720856648, 0.053911238744677341, 0.054169388790072187, 0.054225327665717249]
t4error = [0.037305778172288535, 0.038656191232970684, 0.038656191232970684, 0.021758490353597587, 0.051399290508472972, 0.052726951917367655]

update_figures('Cora', 'Average AUC PR', ylim=aucprmargins)

# IMDB Training Times

t0 = [np.mean([10.881, 9.805, 7.243, 16.201, 18.564, 10.51, 10.877, 7.477, 11.334, 17.821, 10.437, 15.14, 8.603, 12.255, 18.104, 10.027, 9.86, 7.789, 11.567, 17.895, 10.32, 11.677, 8.761, 13.831, 17.644, 10.145, 11.296, 7.417, 14.191, 17.774, 10.957, 11.903, 8.26, 15.224, 15.392, 10.51, 11.118, 8.057, 10.84, 17.153, 9.719, 10.788, 6.832, 11.46, 21.501, 9.778, 12.609, 7.705, 12.093, 14.927])]
t1 = []
t2 = [4.4328399999999997, 4.4889600000000005, 5.3233099999999993, 5.3414799999999989]
t3 = [4.5504799999999994, 6.4588400000000004, 6.5456600000000007, 8.0693199999999994]
t4 = [4.2676600000000002, 6.8454000000000006, 6.7258399999999998, 8.0753599999999999]

t0error = [np.std([10.881, 9.805, 7.243, 16.201, 18.564, 10.51, 10.877, 7.477, 11.334, 17.821, 10.437, 15.14, 8.603, 12.255, 18.104, 10.027, 9.86, 7.789, 11.567, 17.895, 10.32, 11.677, 8.761, 13.831, 17.644, 10.145, 11.296, 7.417, 14.191, 17.774, 10.957, 11.903, 8.26, 15.224, 15.392, 10.51, 11.118, 8.057, 10.84, 17.153, 9.719, 10.788, 6.832, 11.46, 21.501, 9.778, 12.609, 7.705, 12.093, 14.927])]
t1error = []
t2error = [0.60921995568103315, 0.58563292120576693, 1.2739077415181996, 1.5088417046198053]
t3error = [0.43450280735571783, 0.76509759795728027, 0.84298912472225873, 1.6386558569754661]
t4error = [0.62914121181178395, 1.1304431343504191, 0.90657867524004765, 1.3882807030280293]

update_figures('IMDB', 'Average Training Time (s)')

# IMDB AUC ROC

t0 = [np.mean([1.0, 1.0, 0.991949, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.996594, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.991949, 1.0, 1.0, 1.0, 1.0, 0.991949, 1.0, 1.0, 1.0, 1.0, 0.993409, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.991949, 1.0, 1.0])]
t1 = []
t2 = [0.96710644999999984, 0.9676696199999999, 0.97485921999999992, 0.97278001999999997]
t3 = [0.9676696199999999, 0.96965096000000006, 0.96978922000000001, 0.99845472000000002]
t4 = [0.96791273999999983, 0.96983483999999986, 0.96961099999999989, 0.99845352000000009]

t0error = [np.std([1.0, 1.0, 0.991949, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.996594, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.991949, 1.0, 1.0, 1.0, 1.0, 0.991949, 1.0, 1.0, 1.0, 1.0, 0.993409, 1.0, 1.0, 1.0, 1.0, 0.990976, 1.0, 1.0, 1.0, 1.0, 0.991949, 1.0, 1.0])]
t1error = []
t2error = [0.028700524993586794, 0.027978003105218214, 0.026596178732509673, 0.027795599664328166]
t3error = [0.027978003105218214, 0.024473925241333877, 0.024778998010646026, 0.0031148160205058755]
t4error = [0.027060031652464855, 0.024634403008280906, 0.024538237375981178, 0.0031744379990165305]

update_figures('IMDB', 'Average AUC ROC', ylim=aucrocmargins)

# IMDB AUC PR

t0 = [np.mean([1.0, 1.0, 0.95694, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.989562, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.95694, 1.0, 1.0, 1.0, 1.0, 0.95694, 1.0, 1.0, 1.0, 1.0, 0.965715, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.95694, 1.0, 1.0])]
t1 = []
t2 = [0.85913191000000011, 0.86096802000000006, 0.88987989000000012, 0.88249761000000004]
t3 = [0.86096801999999995, 0.86388445999999985, 0.86431069999999988, 0.99187539999999985]
t4 = [0.86061577999999994, 0.86451679999999986, 0.86256851999999995, 0.99205267999999991]

t0error = [np.std([1.0, 1.0, 0.95694, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.989562, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.95694, 1.0, 1.0, 1.0, 1.0, 0.95694, 1.0, 1.0, 1.0, 1.0, 0.965715, 1.0, 1.0, 1.0, 1.0, 0.954219, 1.0, 1.0, 1.0, 1.0, 0.95694, 1.0, 1.0])]
t1error = []
t2error = [0.092933847495096769, 0.092552764268062804, 0.098962445634482477, 0.098491233022527963]
t3error = [0.092552764268062804, 0.096764804190616741, 0.09795141069249591, 0.016551247050298052]
t4error = [0.090979321197795282, 0.097495932081087366, 0.096598151644892258, 0.016543842475604021]

update_figures('IMDB', 'Average AUC PR', ylim=aucprmargins)

#  uwcse training times

t0 = [np.mean([8.472, 8.584, 8.559, 8.598, 9.468, 7.626, 7.838, 9.757, 8.757, 9.24, 9.553, 8.694, 9.246, 9.333, 10.368, 10.019, 8.069, 10.81, 10.292, 9.619, 8.232, 7.688, 8.672, 10.214, 10.643, 9.537, 7.846, 7.983, 9.22, 8.142, 8.697, 8.037, 9.422, 9.235, 8.17, 9.62, 7.955, 9.991, 9.841, 8.979, 9.93, 7.87, 8.123, 8.989, 9.129, 9.125, 9.323, 8.872, 7.883, 8.384])]
t1 = []
t2 = [6.1719299999999988, 6.2610099999999997, 5.9569899999999993, 6.0242899999999997, 6.5251600000000005, 6.5020700000000007, 6.6092699999999986, 6.5091299999999999, 6.74153, 6.4226099999999997, 6.2490400000000008, 5.8136200000000011, 5.8707200000000004, 5.7619299999999987]
t3 = [3.8999599999999996, 3.8185200000000004, 3.7129599999999998, 3.9894600000000002, 3.9952800000000002, 4.1365800000000004, 4.0935200000000007, 4.0930000000000009, 4.1295999999999999, 4.1421400000000004, 4.0566999999999993, 4.1520200000000003, 4.2415799999999999, 4.2464399999999998]
t4 = [3.6431, 3.60168, 3.5926999999999998, 3.9004000000000003, 3.8572199999999999, 3.9682200000000001, 3.98752, 4.1104599999999998, 4.1332399999999998, 4.1886599999999996, 4.0284800000000009, 4.1429, 4.2390799999999995, 4.3097599999999998]

t0error = [np.std([8.472, 8.584, 8.559, 8.598, 9.468, 7.626, 7.838, 9.757, 8.757, 9.24, 9.553, 8.694, 9.246, 9.333, 10.368, 10.019, 8.069, 10.81, 10.292, 9.619, 8.232, 7.688, .672, 10.214, 10.643, 9.537, 7.846, 7.983, 9.22, 8.142, 8.697, 8.037, 9.422, 9.235, 8.17, 9.62, 7.955, 9.991, 9.841, 8.979, 9.93, 7.87, 8.123, 8.989, 9.129, 9.125, 9.323, 8.872, 7.883, 8.384])]
t1error = []
t2error = [0.57528666341225043, 1.1718768407558875, 0.66467717720710096, 0.69066223720426467, 0.82498843288860746, 0.70223613200973922, 0.74223587699598559, 0.65454591366839954, 0.77244557678842329, 0.71149488958108487, 0.80332948308897512, 0.67568178575421134, 0.66262449517053024, 0.96398733658694913]
t3error = [0.42124690906877876, 0.3673572234215628, 0.23417864633650951, 0.27818498953034831, 0.29382035600005657, 0.33246648492742847, 0.31472611839502612, 0.27065372711270763, 0.25129345395373909, 0.30673415264688086, 0.22163774498040725, 0.30451584457955549, 0.27897176129493828, 0.24263513018522273]
t4error = [0.27792461208032659, 0.28074226187020718, 0.2036966617301324, 0.25094883940755736, 0.2635542668977302, 0.27393570705550596, 0.27144282933980779, 0.25084084276688273, 0.31326509923705187, 0.35066009810071058, 0.24586510447804499, 0.30216553410341163, 0.29983421018956458, 0.35066294700181827]

update_figures('UW-CSE', 'Average Training Time (s)')

# uwcse average auc roc

t0 = [np.mean([0.981669, 0.981848, 0.993262, 0.992867, 0.965137, 0.982141, 0.978568, 0.990968, 0.989989, 0.962304, 0.981263, 0.978648, 0.991685, 0.994859, 0.966535, 0.3, 0.980575, 0.995412, 0.993961, 0.962021, 0.976454, 0.975086, 0.993692, 0.994535, 0.960589, 0.978354, 0.976771, 0.995986, 0.993198, 0.96557, 0.984814, 0.983207, 0.995412, 0.99461, 0.967699, 0.985207, 0.976651, 0.992832, 0.995028, 0.962335, 0.981656, 0.976495, 0.995341, 0.994724, 0.967593, 0.981669, 0.977992, 0.998136, 0.99334, 0.965638])]
t1 = []
t2 = [0.96972804999999995, 0.96936338000000011, 0.97044248, 0.97024859999999991, 0.97116515000000003, 0.97085922000000013, 0.97204171000000006, 0.97135055999999975, 0.97189480000000017, 0.97159109999999982, 0.97295139999999991, 0.97286910000000004, 0.97267707000000003, 0.97221581999999995]
t3 = [0.97083712000000011, 0.97076669999999976, 0.9713410400000001, 0.97625965999999986, 0.97677988000000016, 0.97861802000000009, 0.97787888000000012, 0.97825903999999997, 0.97859138000000001, 0.97842837999999999, 0.97864012, 0.97892673999999991, 0.97763822, 0.97839509999999985]
t4 = [0.96925539999999999, 0.96995052000000004, 0.9698873400000001, 0.9768126399999999, 0.97591627999999986, 0.97890810000000006, 0.97748414000000006, 0.97794652000000015, 0.97858619999999985, 0.97733167999999992, 0.97848870000000021, 0.97886771999999989, 0.97847404000000016, 0.97850840000000006]

t0error = [np.std([0.981669, 0.981848, 0.993262, 0.992867, 0.965137, 0.982141, 0.978568, 0.990968, 0.989989, 0.962304, 0.981263, 0.978648, 0.991685, 0.994859, 0.966535, 0.3, 0.980575, 0.995412, 0.993961, 0.962021, 0.976454, 0.975086, 0.993692, 0.994535, 0.960589, 0.978354, 0.976771, 0.995986, 0.993198, 0.96557, 0.984814, 0.983207, 0.995412, 0.99461, 0.967699, 0.985207, 0.976651, 0.992832, 0.995028, 0.962335, 0.981656, 0.976495, 0.995341, 0.994724, 0.967593, 0.981669, 0.977992, 0.998136, 0.99334, 0.965638])]
t1error = []
t2error = [0.012419825747871835, 0.012353021209226506, 0.01265615870197589, 0.012288176734568881, 0.013334174403670442, 0.012844720996253674, 0.013066460948776453, 0.012360280507593665, 0.012562885548312544, 0.012768317313961145, 0.012626062211948744, 0.012949972981825096, 0.013452887412934817, 0.013374029172526881]
t3error = [0.013245213602868018, 0.012723694360129842, 0.012701633008334018, 0.013387431572351728, 0.013808265202609631, 0.012947751407082236, 0.013442182320798957, 0.013812220778658301, 0.014066973246423703, 0.012954932907414068, 0.013123003774502238, 0.013127960007266926, 0.013571622895276744, 0.013636530966855165]
t4error = [0.01299567506365098, 0.011978387082140902, 0.012082746344453315, 0.013378591193036743, 0.013169582316899808, 0.013079680349687442, 0.015128024385239466, 0.01355304300478679, 0.012722741886873277, 0.013703354036789669, 0.013179376120666711, 0.013451648856612345, 0.013353554648796702, 0.013093339150881256]

update_figures('UW-CSE', 'Average AUC ROC', ylim=aucrocmargins)

# uwcse average auc pr

t0 = [np.mean([0.246122, 0.196267, 0.448429, 0.4349, 0.130899, 0.35862, 0.28047, 0.419574, 0.198994, 0.166164, 0.325947, 0.166222, 0.439227, 0.596905, 0.240469, 0.313747, 0.230639, 0.661228, 0.404244, 0.251741, 0.250675, 0.210811, 0.473589, 0.399322, 0.122891, 0.293908, 0.217705, 0.584868, 0.462226, 0.159856, 0.298454, 0.319564, 0.660601, 0.45234, 0.202204, 0.436413, 0.141729, 0.449662, 0.463903, 0.11285, 0.342036, 0.234159, 0.743956, 0.526283, 0.286383, 0.304911, 0.315553, 0.892477, 0.366993, 0.24105])]
t1 = []
t2 = [0.13714956999999997, 0.13772373999999998, 0.15195850000000002, 0.15202962, 0.18089907, 0.16242276000000003, 0.18869625000000004, 0.16920745000000001, 0.17619117000000004, 0.16867054000000001, 0.20528678, 0.20324372999999996, 0.19920148000000004, 0.20290493000000004]
t3 = [0.18994215999999997, 0.17869544000000001, 0.1943955, 0.31881740000000003, 0.32571121999999986, 0.33142910000000003, 0.31291000000000002, 0.33485760000000009, 0.32586669999999995, 0.32629323999999998, 0.30575397999999998, 0.32186862000000005, 0.29919748000000002, 0.3279473]
t4 = [0.14771268000000001, 0.15430709999999997, 0.15336042, 0.30282366000000005, 0.30157264, 0.33338131999999993, 0.33160809999999991, 0.30393972000000002, 0.32006902000000004, 0.30081579999999997, 0.31182655999999997, 0.33602083999999999, 0.32219332000000001, 0.34602874]

t0error = [np.std([0.246122, 0.196267, 0.448429, 0.4349, 0.130899, 0.35862, 0.28047, 0.419574, 0.198994, 0.166164, 0.325947, 0.166222, 0.439227, 0.596905, 0.240469, 0.313747, 0.230639, 0.661228, 0.404244, 0.251741, 0.250675, 0.210811, 0.473589, 0.399322, 0.122891, 0.293908, 0.217705, 0.584868, 0.462226, 0.159856, 0.298454, 0.319564, 0.660601, 0.45234, 0.202204, 0.436413, 0.141729, 0.449662, 0.463903, 0.11285, 0.342036, 0.234159, 0.743956, 0.526283, 0.286383, 0.304911, 0.315553, 0.892477, 0.366993, 0.24105])]
t1error = []
t2error = [0.069139469410208085, 0.074341494932725155, 0.088980604822118406, 0.083644095206389796, 0.12402842774648519, 0.10869611548690412, 0.12870227224593783, 0.099212281053040502, 0.10598637210095033, 0.10191664903885135, 0.12413375800873669, 0.13182363738843311, 0.1308131627826099, 0.13672222780383994]
t3error = [0.13715088910850853, 0.1175855519764499, 0.12394129653464983, 0.13946184570727579, 0.16192355664933872, 0.16932704676173269, 0.17604598929359341, 0.18860272445020512, 0.17291599927967916, 0.16625062995592649, 0.1650645328126536, 0.17725676447502814, 0.16247470570168637, 0.18069717433576543]
t4error = [0.080081754667949173, 0.086678173455432259, 0.093806669576334503, 0.14471527344708435, 0.1281762263998687, 0.16873570739371557, 0.16442274670923729, 0.16346978348490462, 0.1613207844935661, 0.15535837746642439, 0.15866677464474535, 0.17588699762749491, 0.17996172419005549, 0.19048745654628393]

update_figures('UW-CSE', 'Average AUC PR', ylim=aucprmargins)