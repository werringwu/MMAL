# Rebuttal Response to LrXP
We sincerely thank your valuable time and efforts.
## RQ1@Explain mathematical derivation  on local monents.
According to convolution theorem, MMAL Loss $\mathcal{L}$ (Eq.6) computes the amplitude differences, which effectively compares the Fourier transforms of $\mathrm{\mathbf{I}(x,y)·\mathbf{K}(x,y)}$. The modulation map $\mathrm{\mathbf{K}(x,y)}$ built from local moments and a monotonic mapping (Eq.7), encodes structures. A large number of pixel values in $\mathrm{\mathbf{K}(x,y)}$ are relative small , breaking the conditions $\mathrm{\mathbf{I}{(x_1,y_1)}}=\mathrm{\mathbf{I}{(x_2,y_2)}}=\mathrm{\mathbf{I}{(x_3,y_3)}}$ and $\mathrm{\delta_{x_2,y_2,x_3,y_3}}$ in Eq.3 and making amplitude sensitive to local structural changes, where smale pixel values of $\mathrm{\mathbf{I}(x,y)}·\mathrm{\mathbf{K}(x,y)}$ in smooth regions can hardly construct unexcepted coincident solutions. Thus, MMAL enhances structural contrast in the frequency domain.

Tab.1 Diff monotonic.
$g(z)$|$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-|
PSNR↑/SSIM↑|23.92/.922|25.63/.939|26.33/.942|26.63/.944

Tab.2 Ablation study
||w/o g(z)|w/o $M^(2)$|w/o λ|w/o Amp|all
-|-|-|-|-|-
PSNR↑/SSIM↑|22.99/.91|25.91/.941|26.4/.942|25.33/.93|26.63/.944
## RQ2@Evaluate on real-world noisy.
In Tab.3 and Tab.4, MMAL outperforms the baseline (RetinexFormer).

Tab.3 Result of SID/SMID.
| |baseline|MMAL|
-|-|-
SID|24.25/.672|24.34/.673
SMID|29.15/.815|29.28/.816

Tab.4 Noise vs PSNR/SSIM (LOL v2-real).
|$\sigma^2$|0|.02|.04|.06|.1
-|-|-|-|-|-
baseline|22.80/.84|20.74/.694|18.8/.59|17.8/.522|16.29/.277
MMAL|23.21/.875|21.3/.785|19.65/.669|18.93/.582|16.96/.378

## RQ3@Compare with SOTA.
In Tab.5, MMAL outperforms all baselines and RetinexFormer+MMAL surpasses recent methods.

Tab.5 Comparison with SOTA.
PSNR↑/SSIM↑|MambaLLIE'25|FourLLIE'23|WaveMamba'24|Diff-Retinex++'25|RetinexFormer+MMAL
-|-|-|-|-|-
LOLv1|-|20.53/.796|21.02/.808|24.67/.867|25.4/.872
LOLv2-syn|25.87/.94|23.14/.88|23.32/.885|26.06/.944|26.63/.944

## RQ4@compute efficiency.
In Tab.6, MMAL increase a small training time and FLOPS, with any parameter and inference time changed, meeting real-time application.

Tab.6 Diff loss(RetinexFormer,LOLv2-syn).
||Baseline|FFL|LPIPS(VGG)|MMAL
-|-|-|-|-
PSNR↑/SSIM↑|25.67/.93|23.58/.858|26.29.932|26.63/.944
Train/Infer(ms)|48.7/7.2|49.7/7.2|55.2/7.2|54.3/7.2
FLOPS(G)|15.57|15.60|55.68|15.96
Params(M)|1.61|1.61|14.72|1.61
## RQ5@Clarify "semi-local".
Semi-local stats (13x13 windows) encode mid-context, between local ops & global transforms. Lightweight & differentiable, they enable MMK's structure-aware modulation(in Sec. 3.2). The imfact in Tab.2.
## FJ@Overfitting.
Thanks for pointing out. The score of HWMNET was misreported (38.26 to 57.13 ), which without overfitting.


# Rebuttal Response to D8KM
Thank your valuable feedback.
## RQ1@Clarify design motivation and "semi-local".
We discuss unexcepted coincident solutions in Eq.3 with mathematically experssion, where the delicate conditions can be broken by the application of MMK. Meanwhile, the designed MMK introduces structural information into frequency domtain through convolution theorem. Moreover, MMAL uses localized moment statistics to capture structural beyond individual pixels, where continuous features of image moment obtained in adjacent windows ensure capturing semi-local patterns, such as contours of large objects, as shown in Fig.1 and Fig.2.

Tab.1 Diff monotonic.
$g(z)$|$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-|
PSNR↑/SSIM↑|23.92/.922|25.63/.939|26.33/.942|26.63/.944
## RQ2@Extremely low-light with severe noise and failure case.
MMAL enhances low-light images by modulating amplitude based on local intensity variations, making the loss structure-aware and robust to noise. In Fig.4 (5-6th rows, manuscript), MMAL provides cleaner, more detailed results than baseline methods under heavy noise. Tab.2 shows improvements over RetinexFormer under increasing noise. However, baseline models remain brightness discontinuities which MMAL improves structure and reduces noise and still remains a limitation. We aim to address it in future work with noise-handling modules.

Tab.2 Noise vs PSNR/SSIM (LOL v2-real).
|$\sigma^2$|0|.02|.04|.06|.1
-|-|-|-|-|-
baseline|22.80/.84|20.74/.694|18.8/.59|17.8/.522|16.29/.277
MMAL|23.21/.875|21.3/.785|19.65/.669|18.93/.582|16.96/.378
## RQ3@Computational efficiency and real-time performance
In Tab.3, MMAL increase training time and FLOPS slightly, but does't change parameters and inference time, meeting real-time application.

Tab.3 Diff loss funcs(RetinexFormer).
||Baseline|FFL|LPIPS(VGG)|MMAL
-|-|-|-|-
PSNR↑/SSIM↑|25.67/.93|23.58/.858|26.29.932|26.63/.944
Train/Infer(ms)|48.7/7.2|49.7/7.2|55.2/7.2|54.3/7.2
FLOPS(G)|15.57|15.60|55.68|15.96
Params(M)|1.61|1.61|14.72|1.61
## RQ4,RQ5@Comparisons of ablation study.
In Tab.4, removing g(z) causes a large drop in SSIM, highlighting its importance in structure. Removing $M^(2)$ impacts both PSNR and SSIM, indicating their complementary roles in detail preservation. More visual images will be available in open-source repository.
Tab.4 Ablation study
||w/o g(z)|w/o $M^(2)$|w/o λ|w/o Amp|all
-|-|-|-|-|-
PSNR↑/SSIM↑|22.99/.91|25.91/.941|26.4/.942|25.33/.93|26.63/.944
## Additional Comments@missing recent methods.
In Tab.5, MMAL outperforms all baselines and RetinexFormer+MMAL surpasses recent methods.

Tab.5 Comparison with SOTA.
PSNR↑/SSIM↑|MambaLLIE|WaveMamba|Diff-Retinex++|RetinexFormer+MMAL
-|-|-|-|-
LOLv1|-|21.02/.808|24.67/.867|25.4/.872
LOLv2-syn|25.87/.94|23.32/.885|26.06/.944|26.63/.944

# Rebuttal Response to Um3Y
Thank you for valuable time and efforts.
## RQ1@Limited Novelty.
MMAL introduces a novel structure-aware loss by modulating the frequency amplitude using local moments statistics, which encode semi-local structural patterns. Unlike prior frequency-based methods ([15,47]), MMAL uniquely bridges spatial domain statistics and frequency learning through convolution theorem. As stated in Sec. 3.2 (manuscript), to the best of our knowledge, this is the first work to incorporate spatial moments into the loss for LLIE.
Furthermore, we mathematically verify the loss of image details in Eq.3, where the delicate conditions of unexcepted coincident soltuions can be broken by MMK. The MMAL design is model-agnostic, lightweight, and complements both spatial- and frequency-based networks. Across diverse LLIE architectures, this mechanism helps models learn more discriminative representations, leading to improved PSNR/SSIM, shown in Tab.1-2 (manuscript) and Tab.1.

Tab.1 Comparison with SOTA.
PSNR↑/SSIM↑|MambaLLIE'25|FourLLIE'23|FourLLIE+MMAL|WaveMamba'24|WaveMamba+MMAL|Diff-Retinex++'25|RetinexFormer+MMAL
-|-|-|-|-|-|-|-
LOLv1|-|20.53/.796|21.02/.808|21.59/.798|22.09/.815|24.67/.867|25.4/.872
LOLv2-syn|25.87/.94|23.14/.88|23.54/.91|23.32/.885|24.16/.914|26.06/.944|26.63/.944 
## RQ2@Methodological Clarity.
We clarify that MMK is derived by computing local moment statistics over spatial windows, forming a semi-local modulation map as shown in Eq.7. This map scales the frequency amplitude in a structure-aware manner. The choice of $\mathrm{g(z)=\frac{1+z}{2+z}}$ balances non-linearity and boundedness, preserving gradient stability. In Tab.2, we validated this choice against alternatives, and $\mathrm{g(z)}$ yielded consistently better PSNR and SSIM across LLIE tasks.
Tab.2 Diff monotonic.
$g(z)$|$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-|
PSNR↑/SSIM↑|23.92/.922|25.63/.939|26.33/.942|26.63/.944

## RQ3-1@Ablation study on moment order or window size.
In Tab. 4 (manuscript), we have analysis of moment order of the imfact. In the revised manuscript, we have added an analysis of moment order and window size, as shown in Tab.3. We observe that the choice of moment order and window size significantly impacts both PSNR and SSIM in the LOL v2-syn dataset with RetinexFormer+.

Tab.3 Diff kernel size.
Size|5|7|9|11|13|15|17|19|21
-|-|-|-|-|-|-|-|-|-
PSNR↑/SSIM↑|25.8/.94|25.54/.938|26.33/.938|26.1/.941|26.23/.941|26.63/.944|26.04/0.937|25.85/.94|26.01/.94


## RQ3-2@Comparisons with Fourier-domain methods.
In 
We have added comparisons with recent frequence-domain methods, shown in Tab.~\ref{tab:rebuttal_total_compare2}. Our MMAL focuses on constraining the learning process to enhance image quality, and we demonstrate that whether in the frequency domain or spatial domain, our approach consistently outperforms these methods, which mainly rely on frequency domain enhancement. The comparison clearly shows that our method is more effective in improving image quality by enforcing these constraints across both domains.



Tab.4 Comparison with frequency method in LOL v2-syn.
||FECNet|FECNet+MMAL|WaveMamba'24|WaveMamba+MMAL|RetinexFormer+MMAL
-|-|-|-|-|-
PSNR↑/SSIM↑|22.764/.899|23.35/.912|23.32/.885|24.16/.914|26.63/.944

<!-- Tab.4 Comparison with SOTA.
PSNR↑/SSIM↑|MambaLLIE'25|FourLLIE'23|FourLLIE+MMAL|WaveMamba'24|WaveMamba+MMAL|Diff-Retinex++'25|RetinexFormer+MMAL
-|-|-|-|-|-|-|-
LOLv1|-|20.53/.796|21.02/.808|21.59/.798|22.09/.815|24.67/.867|25.4/.872
LOLv2-syn|25.87/.94|23.14/.88|23.54/.91|23.32/.885|24.16/.914|26.06/.944|26.63/.944  -->



# Rebuttal Response to Pudy
Thanks for your valuable time and efforts.
## RQ1@Methodological Clarity & MMK functions justify.
MMAL introduces a novel structure-aware loss by modulating the frequency amplitude using local moments statistics, which encode semi-local structural patterns. MMAL uniquely bridges spatial domain statistics and frequency learning through convolution theorem. Furthermore, we mathematically verify the loss of image details in Eq.3, where the delicate conditions of unexcepted coincident soltuions can be broken by MMK. Specifically, MMK is derived by computing local moment statistics over spatial windows, forming a semi-local modulation map in Eq.7. This map scales the frequency amplitude in a structure-aware manner. The choice of $\mathrm{g(z)}=\frac{1+z}{2+z}$ facilitates invariablitiy of MMK to spatial disturbance as in Fig.2, whose superiority can also be verified by experiments as in Tab.1.



Tab.1 Diff monotonic.
$g(z)$|$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-|
PSNR↑/SSIM↑|23.92/.922|25.63/.939|26.33/.942|26.63/.944
## RQ2@computational complexity.
Thank you for your valuable feedback. We evaluated the computational complexity of MMAL and compared it with other loss functions like FFL and LPIPS (VGG). As shown in Tab.2, MMAL introduces a small increase in training time (54.295 ms) and FLOPs (15.958 G) compared to the baseline (RetinexFormer). However, the parameter count remains unchanged at 1.61M, and the inference time for a 256x256 image is 7.19 ms, which meets real-time requirements. 

Tab.2 Diff loss(RetinexFormer,LOLv2-syn).
||Baseline|FFL|LPIPS(VGG)|MMAL
-|-|-|-|-
PSNR↑/SSIM↑|25.67/.93|23.58/.858|26.29.932|26.63/.944
Train/Infer(ms)|48.7/7.2|49.7/7.2|55.2/7.2|54.3/7.2
FLOPS(G)|15.57|15.60|55.68|15.96
Params(M)|1.61|1.61|14.72|1.61

## Cons3@Discussion of failure cases.
In extreme low-light conditions with high noise, baseline models may result in abnormal brightness discontinuities. While MMAL improves structural details and reduce noise, the brightness discontinuities remain a limitation of the MMAL. We plan to address this in future work by introducing noise-aware modules or improved loss designs.  We'll added this section into the revised manuscript. Additionally, the visuals images will be available in our open-source repository.

## Cons4@Add discussion of related work.
In revised manuscript, we have expanded the discussion of \textit{FourLLIE and other frequency-based[1-3] method, which focuses on frequency-domain information, enhancing global patterns while neglecting local structure and details. These approaches often fails to capture fine image details, which are critical for effective LLIE.}

[1] WaveMamba, 
[2] FourLLIE, 
[3] MambaLLIE,

# Rebuttal Response to ndr8
Thanks for your response.
## RQ1@Theoretical justification of MMK.
<!-- Regarding the modulation function g(z) = (1+z)/(2+z), could you provide theoretical justification for this specific formulation? Have you explored other monotonic functions, and if so, what were the comparative results? -->
The choice of $\mathrm{g(z)}=\frac{1+z}{2+z}$ facilitates invariablitiy of MMK to spatial disturbance as in Fig.2. Specifically, according to the chain rule, the $\frach{1}{(2+z)^2}$ makes relative small values in difference map of image moments caused by spatial disturbances tend to be zero, facilitating invariablitiy to spatial disturbance in optimizating nonlinear continuous network. As shown in Tab.1, we validated this choice against alternatives, and $\mathrm{g(z)}$ consistently achieved the highest PSNR and SSIM across LLIE benchmarks. 

Tab.1 Diff monotonic.
$g(z)$|$\log(1+z)$|$2^z$|$\frac{1}{1+\exp^{-z}}$|$\frac{1+z}{2+z}$
-|-|-|-|-|
PSNR↑/SSIM↑|23.92/.922|25.63/.939|26.33/.942|26.63/.944
## RQ2@Contributions of MMAL.
<!-- Your paper appears to build upon existing techniques in the field. Could you clarify the novel contributions of MMAL compared to previous frequency-domain and moment-based approaches? -->
<!-- MMAL introduces a novel structure-aware loss by modulating the frequency amplitude using local moments statistics, which encode semi-local structural priors. Unlike prior frequency-based methods ([15,47]) that operate on amplitude or phase directly, MMAL uniquely bridges spatial domain statistics and  frequency learning. As stated in Sec. 3.2 (manuscript), to the best of our knowledge, this is the first work to incorporate spatial moments into the loss for LLIE. The MMK through a monotonic function that emphasizes meaningful structure and suppresses noise adaptively—an aspect absent in existing methods. The MMAL design is model-agnostic, lightweight, and complements both spatial- and frequency-based networks. Across diverse LLIE architectures, this mechanism helps models learn more discriminative representations, leading to improved PSNR/SSIM, shown in Tab.1-2 (manuscript) and Tab.2, confirming its novelty and practical value. -->

We propose a novel loss (MMAL) modulating the amplitude spectrum using local moment statistics (Sec.3.2), encoding semi-local structural patterns. This first work incorporating spatial moments into LLIE losses bridges the spatial-frequency domain gap, unlike prior frequency methods[15,47] manipulating amplitude/phase directly. We theoretically analyzes the detail loss of amplitudes, where the delicate conditions can be broken by the designed MMK to reserve image details.
Furthermore the MMK applies a monotonic function on image moments to:
Amplify semantically meaningful structures
Adaptively suppress noise components
– addressing limitations in existing approaches.
Advantages:
• Model-agnostic & lightweight: Compatible with spatial/frequency networks
• Discriminative representation learning: Enhances feature quality across diverse LLV architectures
• Empirically superior: Boosts PSNR/SSIM consistently (Manuscript Tab.1-2, Suppl.Tab.2)
This spatial statistics-guided spectral modulation establishes new SOTA performance with significant practical utility.


Tab.2 Comparison with frequency method in LOL v2-syn.
||FECNet|FECNet+MMAL|FourLLIE'23|FourLLIE+MMAL|WaveMamba'24|WaveMamba+MMAL|RetinexFormer+MMAL
-|-|-|-|-|-|-|-
PSNR↑/SSIM↑|22.764/.899|23.35/.912|23.14/.88|23.54/.91|23.32/.885|24.16/.914|26.63/.944


## RQ3@Comparisons with losses funcs.
<!-- Why didn't you include comparisons with relevant frequency-based loss functions such as Focal Frequency Loss (Jiang et al., 2021) or perceptual metrics like LPIPS with different VGG layers? -->

In Tab.3, MMAL outperforms both FFL and LPIPS(VGG), with better PSNR/SSIM and structure preservation. 

Tab.3 Diff loss(RetinexFormer,LOLv2-syn).
||Baseline|FFL|LPIPS(VGG)|MMAL
-|-|-|-|-
PSNR↑/SSIM↑|25.67/.93|23.58/.858|26.29.932|26.63/.944
Train/Infer(ms)|48.7/7.2|49.7/7.2|55.2/7.2|54.3/7.2
FLOPS(G)|15.57|15.60|55.68|15.96
Params(M)|1.61|1.61|14.72|1.61

## RQ4@comparisons with frequency-domain func.
<!-- Have you considered comparing your approach with other frequency-domain enhancement methods like Wang et al.'s Fourier-based Exposure Correction or Zhang et al.'s Frequency Separation for Enhanced Restoration? -->
MMAL significantly improves baseline performance (Tab.2) and structural benefits beyond frequency priors, approaching RetinexFormer+MMAL.

<!-- In Tab.2, MMAL achieves a significant improvement over the baseline and narrows the gap with our RetinexFormer+. Notably, MMAL consistently brings extra performance gain across both frequency- and spatial- domain networks. -->

<!-- Tab.4 Comparison with frequency method in LOL v2-syn.
||FECNet|FECNet+MMAL|WaveMamba'24|WaveMamba+MMAL|RetinexFormer+MMAL
-|-|-|-|-|-
PSNR↑/SSIM↑|22.764/.899|23.35/.912|23.32/.885|24.16/.914|26.63/.944 -->

## Minor Issues@Writing issues.
<!-- Thank you for your comments. We have clarified the definition of $\sigma^2=0.3$ in Fig.1 (manuscript), explained the notation difference between $\hat{\mathrm{A}}(u,v)$ and ${\mathrm{A}}(u,v)$, and corrected the typos in the revised manuscript. -->
Thanks for pointing out. We have checked and revised the $\sigma^2$ definition, notation consistency, and typos as suggested.
