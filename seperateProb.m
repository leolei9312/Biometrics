function seperateProb(gal, probe, set1, set2)
gallery = load(gal);
prob = load(probe);

veri = {};
recog = {};

[rowProb, colProb] = size(prob.matrix);
[rowGal, colGal] = size(gallery.matrix);
for i = 1 : rowProb
    name = prob.matrix{i, 1};
    eye = prob.matrix{i, 4};
    flag = false;
    for j = 1 : rowGal
        nameGal = gallery.matrix{j, 1};
        eyeGal = gallery.matrix{j, 4};
        if strcmpi(name, nameGal)
            veri = [veri; {prob.matrix{i, 1}, prob.matrix{i, 2}, prob.matrix{i, 3}, prob.matrix{i, 4}}];
            flag = true;
            break;
        end
    end
    if ~flag
        recog = [recog; {prob.matrix{i, 1}, prob.matrix{i, 2}, prob.matrix{i, 3}, prob.matrix{i, 4}}];
    end
end
save(set1,'veri');
save(set2, 'recog');