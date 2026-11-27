# Reproduce the checks

Run `python3 -B -I scripts/verify_repository.py` at the repository root to verify the manifest, hashes and public text scan. Run `python3 -B -I verification/src/replay.py` and compare the three output lines to [the saved replay](verification/logs/replay.txt). Both scripts use the Python standard library.

The replay enumerates the diagonal deck orbit of a base state with the sphere point either polar or nonpolar. It recovers the first return of the first-factor orbit at fixed sphere coordinate and checks the endpoint after each iterate through twice the group order, for cyclic orders from 2 to 64. The existence of a smooth symplectic quotient and the null-homotopy upstairs are mathematical inputs to the proof. The finite checks corroborate the cyclic arithmetic.

[PDF build](paper/BUILD.md) · [Offline illustration](visualization/README.md)
