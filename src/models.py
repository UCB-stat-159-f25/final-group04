from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def _eval_model_core(name, pipe, x_train, y_train, x_valid, y_valid, class_names):
    pipe.fit(x_train, y_train)
    preds = pipe.predict(x_valid)

    acc = accuracy_score(y_valid, preds)
    cm = confusion_matrix(y_valid, preds)

    print("\n" + "=" * 60)
    print(name)
    print(f"accuracy: {acc:.3f}\n")
    print(classification_report(y_valid, preds, target_names=class_names))

    return acc, cm
