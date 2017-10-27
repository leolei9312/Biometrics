% main script

% store template and mask with corresponding subject Id and eye, 
% in form: {subjectId, template,mask, eye}
getTemplate('2008-03-11_13', 'Gallery.mat');
getTemplate('2010-04-27_29', 'Prob1.mat');
getTemplate('2010-04-27_29(1)', 'Prob2.mat');

% extract subjects in gallery from probs
seperateProb('Gallery.mat', 'Prob1.mat', 'VerificationProb1.mat', 'RecognitionProb1.mat');
seperateProb('Gallery.mat', 'Prob2.mat', 'VerificationProb2.mat', 'RecognitionProb2.mat');


% calculate genuine and imposter data for probs
calGenImp('VerificationProb1.mat', 'Gallery.mat', 'GenuineProb1.mat', 'ImposterProb1.mat');
calGenImp('VerificationProb2.mat', 'Gallery.mat', 'GenuineProb2.mat', 'ImposterProb2.mat');

% Draw genuine and imposter distribution and ROC curve from datasets
plotGID('GenuineProb1.mat', 'ImposterProb1.mat');
plotGID('GenuineProb2.mat', 'ImposterProb2.mat');

% Draw CMC curve
plotCMC('VerificationProb1.mat', 'Gallery.mat', 'sortedProb1CMC.mat');
plotCMC('VerificationProb2.mat', 'Gallery.mat', 'sortedProb2CMC.mat');